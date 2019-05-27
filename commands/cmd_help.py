from discord import Embed, Color
import STATICS

def ex(args, message, client, invoke, sender, config):
	if len(args) is 0:
		yield from client.send_message(
				message.channel,
				embed=Embed(
					color=Color.blue(), 
					description=STATICS.HELP.format(
						currency = config['market']['currency'],
						currency2 = config['market']['currency2'],
						bot_name = config['bot']['bot_name'],
						bot_description = config['bot']['bot_description']
						)
					)
				)
	else:
		yield from client.send_message(
			message.channel, 
			embed=Embed(
				color=Color.red(), 
				description=(STATICS.INVALIDHELP)
				)
			)

