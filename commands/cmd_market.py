import ast
import discord
from discord import Embed, Color
from operator import itemgetter, attrgetter, methodcaller
import STATICS

def ex(args, message, client, invoke, sender, config):
    if len(args) is 0:
        buylist = []
        selllist = []

        with open("orderlist.txt") as f:
          for line in f:
            entry = ast.literal_eval(line)
            if entry[0] == 'Buy':
                buylist.append(entry)
            elif entry[0] == 'Sell':
                selllist.append(entry)
            else:
                continue

        buylist = sorted(buylist,key=itemgetter(3))
        selllist = sorted(selllist,key=itemgetter(3))

        sendstr = """-\n:fire: **ORDERBOOK** :fire:\n\n|WTB|"""

        wtb = [0, 0]
        for entry in buylist:
            sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + config['market']['currency'] + ' @ ' + str(entry[3]) + ' ' + config['market']['currency2']
            wtb[0] += float(entry[2])
            wtb[1] += float(entry[2]) * float(entry[3]) / 100000000

        sendstr += "\n> Buy Total {} {}, {} BTC".format(wtb[0], config['market']['currency'], wtb[1])
        sendstr = sendstr + "\n\n" + "|WTS|"

        wts = [0, 0]
        for entry in selllist:
            sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + config['market']['currency'] + ' @ ' + str(entry[3]) + ' ' + config['market']['currency2']
            wts[0] += float(entry[2])
            wts[1] += float(entry[2]) * float(entry[3]) / 100000000

        sendstr += "\n> Sell Total {} {}, {} BTC".format(wts[0], config['market']['currency'], wts[1])

        yield from client.send_message(message.channel, sendstr)
    else:
        yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.INVALIDMARKET)))

