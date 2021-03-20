# All Credits Belong to CipherX and Future Technology Channel 
# Join our channel ~ @FutureTechnologyGuardX
# Copy with Credit 

import asyncio
from telethon import TelegramClient, events, utils, functions, types, connection

print("""   
   _______       __             _  __
  / ____(_)___  / /_  ___  ____| |/ /
 / /   / / __ \/ __ \/ _ \/ ___/   /
/ /___/ / /_/ / / / /  __/ /  /   |
\____/_/ .___/_/ /_/\___/_/  /_/|_|
	  /_/
""") 

api_id = int(input('Enter your account api_id <Get from my.telegram.org>: '))
api_hash = input('Enter your account api_hash <Get from my.telegram.org>: ')
cipherx = TelegramClient("CɪᴘʜᴇʀX", api_id , api_hash )
cipherx.start() 


		
@cipherx.on(events.NewMessage(pattern=r"help"))
async def norouz(event):
	if event.fwd_from:
		return
		await event.edit("راهنمای استفاده از سلف")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>\n5 ~ .msp <count> <reply to gif/sticker/video/picture>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>\n5 ~ .msp <count> <reply to gif/sticker/video/picture>\n6 ~ .1font <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>\n5 ~ .msp <count> <reply to gif/sticker/video/picture>\n6 ~ .1font <text>\n7 ~ .2font <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>\n5 ~ .msp <count> <reply to gif/sticker/video/picture>\n6 ~ .1font <text>\n7 ~ .2font <text>\n8 ~ .3font <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>\n5 ~ .msp <count> <reply to gif/sticker/video/picture>\n6 ~ .1font <text>\n7 ~ .2font <text>\n8 ~ .3font <text>\n9 ~ .4font <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>\n5 ~ .msp <count> <reply to gif/sticker/video/picture>\n6 ~ .1font <text>\n7 ~ .2font <text>\n8 ~ .3font <text>\n9 ~ .4font <text>\n10 ~ .5font <text>")
		await event.edit("راهنمای استفاده از سلف\n✨لیست کامند ها:\n1 ~ .type <text>\n2 ~ .norouz\n3 ~ .sp < count<100 > <text>\n4 ~ .bigsp < count>100 > <text>\n5 ~ .msp <count> <reply to gif/sticker/video/picture>\n6 ~ .1font <text>\n7 ~ .2font <text>\n8 ~ .3font <text>\n9 ~ .4font <text>\n10 ~ .5font <text>\n✨(c) @FutureTechnologyGuardX Exclusive✨")

@cipherx.on(events.NewMessage(pattern="^.type (.*)"))
async def typewriter(event):
	if event.fwd_from:
		return
	input_str = event.pattern_match.group(1)
	cipherxbot = "\u2060"
	for i in range(601):
		cipherxbot += "\u2060"
	try:
		await event.edit(cipherxbot)
	except Exception as e:
		logger.warn(str(e))
	typing_symbol = "|"
	delay = 0.03
	previous_text = ""
	await event.edit(typing_symbol)
	await asyncio.sleep(delay)
	for character in input_str:
		previous_text = previous_text + "" + character
		typing_text = previous_text + "" + typing_symbol
		try:
			await event.edit(typing_text)
		except Exception as e:
			logger.warn(str(e))
		await asyncio.sleep(delay)
		try:
			await event.edit(previous_text)
		except Exception as e:
			logger.warn(str(e))
		await asyncio.sleep(delay)
		
@cipherx.on(events.NewMessage(pattern=r"norouz"))
async def norouz(event):
	if event.fwd_from:
		return
	if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
		await event.edit("💜💜                           💜💜\n💜💜💜                       💜💜\n💜💜💜💜                 💜💜\n💜💜  💜💜               💜💜\n💜💜     💜💜            💜💜\n💜💜         💜💜        💜💜\n💜💜             💜💜    💜💜\n💜💜                 💜💜💜💜\n💜💜                     💜💜💜\n💜💜                          💜💜")
		await event.edit("          💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖")
		await event.edit("💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                     💙💙\n💙💙                     💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n💙💙    💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                  💙💙")
		await event.edit("          💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖")
		await event.edit("💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n  💜💜                  💜💜\n      💜💜💜💜💜💜\n            💜💜💜💜")
		await event.edit(" 💟💟💟💟💟💟💟\n 💟💟💟💟💟💟💟\n                       💟💟\n                   💟💟\n               💟💟\n           💟💟\n       💟💟\n   💟💟\n💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟")
		await event.edit("💚💚                              💚💚\n💚💚💚                      💚💚💚\n💚💚💚💚            💚💚💚💚\n💚💚    💚💚    💚💚    💚💚\n💚💚        💚💚💚        💚💚\n💚💚             💚             💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚")
		await event.edit("          💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖")
		await event.edit("💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗")
		await event.edit("                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖")
		await event.edit("💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                     💙💙\n💙💙                     💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n💙💙    💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                  💙💙")
		await event.edit("                   💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖")
		await event.edit("💙💙                  💙💙\n💙💙             💙💙\n💙💙        💙💙\n💙💙   💙💙\n💙💙💙💙\n💙💙 💙💙\n💙💙     💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                   💙💙")
		await event.edit("Ⲏ")
		await event.edit("Ⲏⲁ")
		await event.edit("Ⲏⲁⲣ")
		await event.edit("Ⲏⲁⲣⲣ")
		await event.edit("Ⲏⲁⲣⲣⲩ")
		await event.edit("Ⲏⲁⲣⲣⲩ ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇ")
		await event.edit("Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ")
		await event.edit("💛💛Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💛💛")
		await event.edit("💝💝Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💝💝")
		await event.edit("💓💓Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💓💓")
		await event.edit("💗💗Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💗💗")
		await event.edit("💞💞Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💞💞")
		await event.edit("💖💖Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💖💖")
		await event.edit("💙💙Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💙💙")
		await event.edit("💘💘Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💘💘")
		await event.edit("💕💕Ⲏⲁⲣⲣⲩ Ⲛⲟʀⲟυⲍ ⲧⲟ Ⲉⳳⲉʀⲩⲃⲟⲇⲩ💕💕")

@cipherx.on(events.NewMessage(pattern="^.sp (.*)"))
async def minorspam(e):
	if event.fwd_from:
		return
	sender = await e.get_sender() ; me = await e.client.get_me()
	try:
		await e.delete()
	except:
		pass
	try:
		counter = int(e.pattern_match.group(1).split(' ', 1)[0])
		spam_message = str(e.pattern_match.group(1).split(' ', 1)[1])
		await asyncio.wait([e.respond(spam_message) for i in range(counter)])
	except:
		return await e.reply(
			f"**ارور**\nنحوه استفاده: `.sp <تعداد کمتر از 100> متن`"
		)

@cipherx.on(events.NewMessage(pattern="^.bigsp (.*)"))
async def bigspam(e):
	if event.fwd_from:
		return
	try:
		await e.delete()
	except:
		pass
	if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
		message = e.text
		counter = int(message[9:13])
		spam_message = str(e.text[13:])
		for i in range(1, counter):
			await e.respond(spam_message)
	else:
		return await e.reply(
			f"**ارور**\nنحوه استفاده: `.bigsp <تعداد بالاتر از 100> متن`"
		)

@cipherx.on(events.NewMessage(pattern="^.msp (.*)"))
async def picspam(e):
	if event.fwd_from:
		return
	sender = await e.get_sender()
	me = await e.client.get_me()
	try:
		await e.delete()
	except:
		pass
	try:
		counter = int(e.pattern_match.group(1).split(" ", 1)[0])
		reply_message = await e.get_reply_message()
		if (
			not reply_message
			or not e.reply_to_msg_id
			or not reply_message.media
			or not reply_message.media
		):
			return await e.edit("```روی یک عکس، گیف، استیکر و یا ویدئو ریپلای کنید و کامند را بزنید.```")
		message = reply_message.media
		for i in range(1, counter):
			await e.client.send_file(e.chat_id, message)
	except:
		return await e.reply(
			f"**ارور**\nنحوه استفاده: `.msp <تعداد> ریپلای رو گیف/استیکر/عکس/ویدئو`"
		)

####fonts###

ormiefont = [
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i",
	"j",
	"k",
	"l",
	"m",
	"n",
	"o",
	"p",
	"q",
	"r",
	"s",
	"t",
	"u",
	"v",
	"w",
	"x",
	"y",
	"z",
]
irclefont = [
	"a⃠",
	"b⃠",
	"c⃠",
	"d⃠",
	"e⃠",
	"f⃠",
	"g⃠",
	"h⃠",
	"i⃠",
	"j⃠",
	"k⃠",
	"l⃠",
	"m⃠",
	"n⃠",
	"o⃠",
	"p⃠",
	"q⃠",
	"r⃠",
	"s⃠",
	"t⃠",
	"u⃠",
	"v⃠",
	"w⃠",
	"x⃠",
	"y⃠",
	"z⃠",
]



nnormiefont = [
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i",
	"j",
	"k",
	"l",
	"m",
	"n",
	"o",
	"p",
	"q",
	"r",
	"s",
	"t",
	"u",
	"v",
	"w",
	"x",
	"y",
	"z",
]
ccirclefont = [
	"𝖆",
	"𝖇",
	"𝖈",
	"𝖉",
	"𝖊",
	"𝖋",
	"𝖌",
	"𝖍",
	"𝖎",
	"𝖏",
	"𝖐",
	"𝖑",
	"𝖒",
	"𝖓",
	"𝖔",
	"𝖕",
	"𝖖",
	"𝖗",
	"𝖘",
	"𝖙",
	"𝖚",
	"𝖛",
	"𝖜",
	"𝖝",
	"𝖞",
	"𝖟",
]




normiefont = [
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i",
	"j",
	"k",
	"l",
	"m",
	"n",
	"o",
	"p",
	"q",
	"r",
	"s",
	"t",
	"u",
	"v",
	"w",
	"x",
	"y",
	"z",
]
circlefont = [
	"𝓪",
	"𝓫",
	"𝓬",
	"𝓭",
	"𝓮",
	"𝓯",
	"𝓰",
	"𝓱",
	"𝓲",
	"𝓳",
	"𝓴",
	"𝓵",
	"𝓶",
	"𝓷",
	"𝓸",
	"𝓹",
	"𝓺",
	"𝓻",
	"𝓼",
	"𝓽",
	"𝓾",
	"𝓿",
	"𝔀",
	"𝔁",
	"𝔂",
	"𝔃",
]



onormiefont = [
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i",
	"j",
	"k",
	"l",
	"m",
	"n",
	"o",
	"p",
	"q",
	"r",
	"s",
	"t",
	"u",
	"v",
	"w",
	"x",
	"y",
	"z",
]
ocirclefont = [
	"🅰",
	"🅱",
	"🅲",
	"🅳",
	"🅴",
	"🅵",
	"🅶",
	"🅷",
	"🅸",
	"🅹",
	"🅺",
	"🅻",
	"🅼",
	"🅽",
	"🅾",
	"🅿",
	"🆀",
	"🆁",
	"🆂",
	"🆃",
	"🆄",
	"🆅",
	"🆆",
	"🆇",
	"🆈",
	"🆉",
]



anormiefont = [
	"a",
	"b",
	"c",
	"d",
	"e",
	"f",
	"g",
	"h",
	"i",
	"j",
	"k",
	"l",
	"m",
	"n",
	"o",
	"p",
	"q",
	"r",
	"s",
	"t",
	"u",
	"v",
	"w",
	"x",
	"y",
	"z",
]
acirclefont = [
	"🄰",
	"🄱",
	"🄲",
	"🄳",
	"🄴",
	"🄵",
	"🄶",
	"🄷",
	"🄸",
	"🄹",
	"🄺",
	"🄻",
	"🄼",
	"🄽",
	"🄾",
	"🄿",
	"🅀",
	"🅁",
	"🅂",
	"🅃",
	"🅄",
	"🅅",
	"🅆",
	"🅇",
	"🅈",
	"🅉",
]
###fonts###


@cipherx.on(events.NewMessage(pattern="1font ?(.*)"))
async def weebify(event):
	if event.fwd_from:
		return
	args = event.pattern_match.group(1)
	if not args:
		get = await event.get_reply_message()
		args = get.text
	if not args:
		await event.edit("`یه متن بده بهم`")
		return
	string = "  ".join(args).lower()
	for ormiecharacter in string:
		if ormiecharacter in ormiefont:
			irclecharacter = irclefont[ormiefont.index(ormiecharacter)]
			string = string.replace(ormiecharacter, irclecharacter)
	await event.edit(string)


@cipherx.on(events.NewMessage(pattern="2font ?(.*)"))
async def weebify(event):
	if event.fwd_from:
		return
	args = event.pattern_match.group(1)
	if not args:
		get = await event.get_reply_message()
		args = get.text
	if not args:
		await event.edit("`یه متن بده بهم`")
		return
	string = "  ".join(args).lower()
	for nnormiecharacter in string:
		if nnormiecharacter in nnormiefont:
			ccirclecharacter = ccirclefont[nnormiefont.index(nnormiecharacter)]
			string = string.replace(nnormiecharacter, ccirclecharacter)
	await event.edit(string)

@cipherx.on(events.NewMessage(pattern="3font ?(.*)"))
async def weebify(event):
	if event.fwd_from:
		return
	args = event.pattern_match.group(1)
	if not args:
		get = await event.get_reply_message()
		args = get.text
	if not args:
		await event.edit("`یه متن بده بهم`")
		return
	string = "  ".join(args).lower()
	for normiecharacter in string:
		if normiecharacter in normiefont:
			circlecharacter = circlefont[normiefont.index(normiecharacter)]
			string = string.replace(normiecharacter, circlecharacter)
	await event.edit(string)


@cipherx.on(events.NewMessage(pattern="4font ?(.*)"))
async def weebify(event):
	if event.fwd_from:
		return
	args = event.pattern_match.group(1)
	if not args:
		get = await event.get_reply_message()
		args = get.text
	if not args:
		await event.edit("`یه متن بده بهم`")
		return
	string = "  ".join(args).lower()
	for onormiecharacter in string:
		if onormiecharacter in onormiefont:
			ocirclecharacter = ocirclefont[onormiefont.index(onormiecharacter)]
			string = string.replace(onormiecharacter, ocirclecharacter)
	await event.edit(string)

@cipherx.on(events.NewMessage(pattern="5font ?(.*)"))
async def weebify(event):
	if event.fwd_from:
		return
	args = event.pattern_match.group(1)
	if not args:
		get = await event.get_reply_message()
		args = get.text
	if not args:
		await event.edit("`یه متن بده بهم`")
		return
	string = "  ".join(args).lower()
	for anormiecharacter in string:
		if anormiecharacter in anormiefont:
			acirclecharacter = acirclefont[anormiefont.index(anormiecharacter)]
			string = string.replace(anormiecharacter, acirclecharacter)
	await event.edit(string)

get_event_loop().run_forever()        
cipherx.run_until_disconeccted() 
