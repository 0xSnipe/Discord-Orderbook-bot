# Discord Orderbook bot
The next generation Veles Core discord orderbook bot. Based on the bot originally made for the Nyzo project with patches ported from Bismuth Foundation.

Can be used for any type of discord channel where an orderbook bot is necessary.
Uses the discord.py library.

## Install
Needs python3

- Copy bot.conf.example to bot.conf and update to your needs to get started.
- Install requirements `pip3 install -r requirements.txt`
- run main.py `python3 main.py`

Some supervisor or cron helper could be needed to restart the bot should it crash.

## Privileged commands
To use privileged commands, set bot_masters configuration option according to the example config.
Currently following privileged command is supported:
`!delegate NICK#ID COMMAND ARGS`
This will run COMMAND with ARGS as NICK, plase use full form of Discord username as when mentioning (only without @ as the at sign would trigger Discord's internal mention handling), 
for example:
`!delegate AltcoinBaggins#6959 !wtb 10000 1500` 

## History
Veles Core next-gen fork
- added support for easy configuration using standard ini-style config file, see bot.conf.example
- refactored main script into class for better OOP
- better language string formating using placeholders (eg. {currency}, {currency2} ...)
- support also channel names instead of just IDs
- possibility to configure commands that can be used also without a prefix (eg. wtb, wts)
- added command !price to report on price information from coinmarketcap or compatible API
- possibility to configure presence message (game name)
- new configuration option bot_masters to specify usernames that are able to run privileged commands
- added privileged command !delegate to execute command on behalf of other user

Bismuth version Public release
- removes some hardcoded Nyzo strings
- limit commands to specific channels only
- add WTS total and WTB Total
- clean up repo with .gitignore
- add requirements.txt
