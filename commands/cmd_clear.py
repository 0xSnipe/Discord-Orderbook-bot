import ast
import discord
from discord import Embed, Color
import STATICS
import fileinput

from commands import cmd_market

def ex(args, message, client, invoke, sender, config):

    if len(args) is 0:
        sendstr = """-\n:fire: **ORDERBOOK** :fire:\n\n|WTB|"""

        for line in fileinput.input("orderlist.txt", inplace =1):
            entry = ast.literal_eval(line)
            line = line.strip()
            if not entry[1] == sender in line:
                print(line)
            else:
                continue

        sendstr = "Cleared **" + sender[:-5] + "**'s orders."

        yield from client.send_message(message.channel, sendstr)
        yield from cmd_market.ex(args, message, client, invoke, sender, config)

    else:
        yield from client.send_message(message.channel, STATICS.INVALIDCLEAR)
