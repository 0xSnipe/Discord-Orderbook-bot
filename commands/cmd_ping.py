import discord

def ex(args, message, client, invoke, sender, config):
    yield from client.send_message(message.channel, "Pong")