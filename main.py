import asyncio as asyncio
import discord
from discord import Game, Server, Member, Embed, Color
import configparser, os
import argparse, sys

from commands import cmd_ping, cmd_wtb, cmd_wts, cmd_market, cmd_help, cmd_clear, cmd_price

class ConfigurationError(ValueError):
    '''raise this when there's a critical error with the configuration file'''

class DiscordOrderbookBot(object):
    commands = {
        "ping": cmd_ping,
        "wtb": cmd_wtb,
        "wts": cmd_wts,
        "market": cmd_market,
        "help": cmd_help,
        "clear": cmd_clear
    }

    def __init__(self, config_file = 'bot.conf'):
        if not os.path.isfile(config_file):
            raise ConfigurationError('Configuration file not found: {}\n'
                + 'See "bot.conf.example" for a defaut configuration.'.format(os.path.abspath(config_file)))

        self.config = configparser.ConfigParser()
        self.config.read(config_file)

        if not 'token' in self.config['secrets'] or not self.config['secrets']['token']:
            raise ConfigurationError('Value for "token" configuration option not found, please edit your bot.conf')

        self.client = discord.Client()
        self.client.on_ready = self.on_ready
        self.client.on_message = self.on_message

        # Commands that are enabled according to the config
        if 'cmc_api_url' in self.config['market'] and self.config['market']['cmc_api_url']:
            self.commands['price'] = cmd_price

    def run(self):
        self.client.run(self.config['secrets']['token'])

    @asyncio.coroutine
    def on_ready(self):
        print("Bot is logged in succesfully. Running on servers: \n")
        for s in self.client.servers:
            print(" - %s (%s)" % (s.name, s.id))

        if 'presence_game' in self.config['bot']:
            yield from self.client.change_presence(game=Game(name=self.config['bot']['presence_game']))

    @asyncio.coroutine
    def on_message(self, message):
        # Allow some special commands also without prefix
        if ('allow_no_prefix' in self.config['bot']
                and message.content.split(" ")[0].lower() in self.config['bot']['allow_no_prefix'].split('\n')):
            message.content = self.config['bot']['prefix'] + message.content;

        if message.content.startswith(self.config['bot']['prefix']):
            # support channel ids and channel names as well (and long line format as for PEP8)
            if (message.server and 'auth_channels' in self.config['bot']     # when commented out in config, listen on all channels
                    and message.channel.id not in self.config['bot']['auth_channels'].split('\n')   # support multi-line values
                    and message.channel.name not in self.config['bot']['auth_channels'].split('\n')
                    ): 
                print('Unsupported channel: %s (%i)'.format(message.channel.name, message.channel.id))
                return

            sender = str(message.author)
            invoke = message.content[len(self.config['bot']['prefix']):].split(" ")[0].lower()
            args = message.content.split(" ")[1:]
            print("INVOKE: %s\nARGS: %s" % (invoke, args.__str__()[1:-1].replace("'","")))

            # Allow bot masters to send a command on behalf of other user using "delegate" command
            # using syntax    !delegate username command args   (when ! is prefix)
            if invoke == 'delegate' and 'bot_masters' in self.config['bot'] and sender in self.config['bot']['bot_masters'].split('\n'):
                sender = args.pop(0)
                invoke = args.pop(0)

                # Be more robust and allow delegating commands both with or without prefix
                if invoke.startswith(self.config['bot']['prefix']):
                    invoke = invoke[len(self.config['bot']['prefix']):]

            if self.commands.__contains__(invoke):
                yield from self.commands.get(invoke).ex(args, message, self.client, invoke, sender, self.config)
            else:
                yield from self.client.send_message(message.channel, embed=Embed(color=Color.red(), description=("The command '%s' is not valid." % invoke)))
                #to send a message to the author directly: yield from client.send_message(message.author, embed=Embed(color=Color.red(), description=("The command '%s' is not valid." % invoke)))

def main():
    parser = argparse.ArgumentParser(description='Discord Orderbook Bot.')
    parser.add_argument('--config', default='bot.conf',
                    help='path to the configuration file')
    args = parser.parse_args()
    
    try:
        app = DiscordOrderbookBot(config_file = args.config)
        app.run()
    except ConfigurationError as err:
        print("DiscordOrderbookBot: Error: {}".format(err.args[0]))
        sys.exit(1)

if __name__=='__main__':
    main()
