INVALIDMARKET = "No such market found.\nCorrect format: !market"
INVALIDHELP = "Try using '!help' instead."
INVALIDCLEAR = "Try using '!clear' instead."
INMAX= "Maximum amount of orders per user: {maxorders}"
HELP_WTB = "Correct format: !wtb AMOUNT-{currency} AMOUNT-{currency2}\nEx. !wtb 1000 500"
HELP_WTS = "Correct format: !wts AMOUNT-{currency} AMOUNT-{currency2}\nEx. !wtb 1000 500"
HELP = "**This is {bot_name}, {bot_description}**\n\nCommands:\n!wtb AMOUNT-{currency} AMOUNT-{currency2}\n!wts AMOUNT-{currency} AMOUNT-{currency2}\n!market\n!clear\n!price\n\nFor buy and sell orders, fill in the {currency2} price **per** {currency}."
PRICE_INFO = """Recent average price information on {symbol}:\n
Price: 		**{price_btc}** BTC, **{price_usd}** USD
Market cap: **{market_cap_usd}** USD
Change 24h:	**{percent_change_24h}**%
Change 7d:	**{percent_change_7d}**%
"""
PRICE_ERROR = "Sorry, I'm unable to fetch price information right now, please try again later on."