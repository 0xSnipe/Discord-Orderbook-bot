import ast
import discord
from discord import Embed, Color
from operator import itemgetter, attrgetter, methodcaller
import STATICS

def ex(args, message, client, invoke, sender, config):
    if len(args) is 2:
        amtcurrency = args[0]
        amtsats = args[1]
        try:
            amtcurrency = float(amtcurrency)
            amtsats = float(amtsats)
        except:
            # yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.HELPER)))
            print('No numbers')

        with open("orderlist.txt") as f:
            count = 0
            for line in f:
                entry = ast.literal_eval(line)
                if entry[1] == sender in line:
                    count = count + 1

        if count < int(config['market']['maxorders']):
            if type(amtcurrency) is float and type(amtsats) is float:
                if amtcurrency > 0 and amtsats > 0:
                    cal = round((amtcurrency * amtsats) / 100000000, 8)
                    cal = format(cal, '.8f')
                    sendstr = """-\n:loudspeaker: New order added: \n**Buy** {0} {3} for {1} sats each = {2} BTC\n\n:fire: **ORDERBOOK** :fire:\n\n|WTB|""".format(
                        amtcurrency, amtsats, cal, config['market']['currency'])

                    neworder = ['Buy', sender, amtcurrency, amtsats, cal]
                    with open("orderlist.txt", "a") as f:
                        f.write("{}".format(neworder))
                        f.write("\n")

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

                    for entry in buylist:
                        sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + config['market']['currency'] + ' @ ' + str(entry[3]) + ' ' + config['market']['currency2']

                    sendstr = sendstr + "\n\n" + "|WTS|"

                    for entry in selllist:
                        sendstr = sendstr + "\n" + str(entry[1])[:-5] + " - " + str(entry[2]) + ' ' + config['market']['currency'] + ' @ ' + str(entry[3]) + ' ' + config['market']['currency2']

                    yield from client.send_message(message.channel, sendstr)
                else:
                    yield from client.send_message(message.channel,
                            embed=Embed(color=Color.red(), description=(STATICS.HELP_WTB.format(
                                currency = config['market']['currency'],
                                currency2 = config['market']['currency2']))))

            else:
                yield from client.send_message(message.channel,
                        embed=Embed(color=Color.red(), description=(STATICS.HELP_WTB.format(
                            currency = config['market']['currency'],
                            currency2 = config['market']['currency2']))))

        elif count >= int(config['market']['maxorders']):
            yield from client.send_message(message.channel, embed=Embed(
                    color=Color.red(), 
                    description=(STATICS.INMAX.format(maxorders = int(config['market']['maxorders'])))))
    else:
        yield from client.send_message(message.channel, embed=Embed(color=Color.red(), description=(STATICS.HELP_WTB.format(
                currency = config['market']['currency'],
                currency2 = config['market']['currency2']))))
