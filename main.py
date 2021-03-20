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
        await event.edit("💜💜                           💜💜\n💜💜💜                       💜💜\n💜💜💜💜                 💜💜\n💜💜  💜💜               💜💜\n💜💜     💜💜            💜💜\n💜💜         💜💜        💜💜\n💜💜             💜💜    💜💜\n💜💜                 💜💜💜💜\n💜💜                     💜💜💜\n💜💜                          💜💜")
⁭        await asyncio.sleep(0.5)
        await event.edit("          💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖")
⁭        await asyncio.sleep(0.5)
        await event.edit("💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                     💙💙\n💙💙                     💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n💙💙    💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                  💙💙")
⁭        await asyncio.sleep(0.5)
        await event.edit("          💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖")
⁭        await asyncio.sleep(0.5)
        await event.edit("💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n💜💜                      💜💜\n  💜💜                  💜💜\n      💜💜💜💜💜💜\n            💜💜💜💜")
⁭        await asyncio.sleep(0.5)
        await event.edit(" 💟💟💟💟💟💟💟\n 💟💟💟💟💟💟💟\n                       💟💟\n                   💟💟\n               💟💟\n           💟💟\n       💟💟\n   💟💟\n💟💟💟💟💟💟💟\n💟💟💟💟💟💟💟")
        await asyncio.sleep(0.5)
        await event.edit("💚💚                              💚💚\n💚💚💚                      💚💚💚\n💚💚💚💚            💚💚💚💚\n💚💚    💚💚    💚💚    💚💚\n💚💚        💚💚💚        💚💚\n💚💚             💚             💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚\n💚💚                              💚💚")
⁭        await asyncio.sleep(0.5)
        await event.edit("          💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                   💖💖\n 💖💖                       💖💖\n💖💖                         💖💖\n💖💖                         💖💖\n 💖💖                       💖💖\n   💖💖                   💖💖\n      💖💖💖💖💖💖💖\n            💖💖💖💖💖")
⁭        await asyncio.sleep(0.5)
        await event.edit("💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗💗\n💗💗                     💗💗\n💗💗                     💗💗\n💗💗💗💗💗💗💗💗\n💗💗💗💗💗💗💗")
        await asyncio.sleep(0.5)
        await event.edit("                    💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖")
⁭        await asyncio.sleep(0.5)
        await event.edit("💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙💙\n💙💙                     💙💙\n💙💙                     💙💙\n💙💙💙💙💙💙💙💙\n💙💙💙💙💙💙💙\n💙💙    💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                  💙💙")
⁭        await asyncio.sleep(0.5)
        await event.edit("                   💖\n                  💖💖\n               💖💖💖\n            💖💖 💖💖\n          💖💖    💖💖\n        💖💖       💖💖\n      💖💖💖💖💖💖\n     💖💖💖💖💖💖💖\n   💖💖                 💖💖\n  💖💖                    💖💖\n💖💖                       💖💖")
⁭        await asyncio.sleep(0.5)
        await event.edit("💙💙                  💙💙\n💙💙             💙💙\n💙💙        💙💙\n💙💙   💙💙\n💙💙💙💙\n💙💙 💙💙\n💙💙     💙💙\n💙💙         💙💙\n💙💙              💙💙\n💙💙                   💙💙")
        await asyncio.sleep(0.5)
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
async def spammer(e):
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
        
@cipherx.on(events.NewMessage(pattern="^.bigsp (.*)"))
async def bigspam(e):
    if not e.text[0].isalpha() and e.text[0] not in ("/", "#", "@", "!"):
        message = e.text
        counter = int(message[9:13])
        spam_message = str(e.text[13:])
        await e.delete()
        for i in range(1, counter):
            await e.respond(spam_message)

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


get_event_loop().run_forever()        
cipherx.run_until_disconeccted() 
