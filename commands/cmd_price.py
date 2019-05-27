from discord import Embed, Color
import STATICS
import requests, json

def ex(args, message, client, invoke, sender, config):
	try:
		response = requests.get(config['market']['cmc_api_url'])
		data = json.loads(response.content.decode())[0]

		yield from client.send_message(
				message.channel,
				embed=Embed(
					color=Color.green(), 
					description=STATICS.PRICE_INFO.format(**data)
					)
				)
	except:
		yield from client.send_message(
			message.channel, 
			embed=Embed(
				color=Color.red(), 
				description=(STATICS.PRICE_ERROR)
				)
			)

