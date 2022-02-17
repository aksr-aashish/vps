#same on telethon 
from dataclasses import dataclass
from datetime import datetime
from multiprocessing import Event
from telethon import events, Button,custom, events, Button ,__version__
from telethon import TelegramClient
import logging,time,logging,asyncio,sys,telethon,asyncio,requests,os,json
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from psutil import cpu_percent, virtual_memory, disk_usage, boot_time
import os, re, time
from telethon.tl.types import PeerUser
from typing import List, Optional


logging.basicConfig(
    level=logging.INFO, format="[%(levelname)s] %(asctime)s - %(message)s"
)
LOGGER = logging.getLogger(__name__)
LOGGER.info("Vexana Fanclub is starting. | An VexanaFanClub Project. | Licensed under GPLv3.")
LOGGER.info("Not affiliated to Shie Hashaikai or Villain in any way whatsoever.")
LOGGER.info("Project maintained by: Itzz_axel11 (t.me/Itzz_Axel)")
log = logging.getLogger("Vexana X FanClub Server")

log.info("\n\nLoading basic info...")
log.info("\n\nStarting...\n")

# getting the vars
try:
    API_ID = 2984107
    API_HASH = "4ce83ad7d954da391c659c6d7d76e0ce"
    BOT_TOKEN = "5160100610:AAHoLVXbu9dm-ac1wJl6Kd___7meZSz68eU" #os.environ.get("BOT_TOKEN", None)
    SUDOERS = os.environ.get("SUDOERS", None)
    OWNER_ID = [5086015489,5001573230, 5086015489]
except Exception as e:
    log.warning("Missing config vars {}".format(e))
    exit(1)    

try:
    bot = TelegramClient(None, 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(
        bot_token=BOT_TOKEN
    )
except Exception as e:
    log.exception(e)
    exit(1)




@bot.on(events.NewMessage(incoming=True, pattern="/support"))
async def support(event):
    await event.reply("Hello!",
                    buttons=[
                        [Button.url("Owner", url="https://t.me/axel_0p")],
                        [Button.url("Support",url="https://t.me/vexana_Support")]
                    ])


@bot.on(events.NewMessage(incoming=True, pattern="/id"))
async def ids(event):
    axelbot = await bot.get_me()
    bot_id = axelbot.first_name
    bot_username = axelbot.username
    reply = await event.client(GetFullUserRequest(event.sender_id))
    firstname = reply.user.first_name
    vent = event.chat_id
    await event.reply(f"**Your ID**: `{event.sender_id}`\n**Chat ID**: `{vent}`\n**Your Name**: `{firstname}`")

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, obtained = divmod(seconds, 60)
        else:
            remainder, obtained = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(obtained))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time
    
#Uptime
bot_start_time = time.time()
bot_uptime = int(time.time() - bot_start_time)
@bot.on(events.NewMessage(incoming=True, pattern="/stats"))
async def ping(event):
    ram = virtual_memory()
    cpu = cpu_percent()
    disk = disk_usage("/")
    text = "*>-------< System >-------<*\n\n"
    text += f"Uptime: `{get_readable_time((bot_uptime))}`\n"
    text += f"**CPU:** `{cpu}%`\n"
    text += f"**RAM:** `{ram}%`\n"
    text += f"**Disk:** `{disk}%`\n"
    text += f"**Python Version:** `3.10.0`\n"
    text += "**Library:** `Pyrogram`\n"
    text += f"**Telethon Version:** `{__version__}`"
    await event.reply(text, parse_mode="markdown")

@bot.on(events.NewMessage(incoming=True, pattern="/ping"))
async def ping(e):
    if e.reply_to_msg_id:
        fuk = await e.respond("Pᴏɴɢ!!.....", reply_to=e.reply_to_msg_id)
    else:
        fuk = await e.reply("Pᴏɴɢ!!.....")
        start = datetime.now()
        end = datetime.now()
        ms = (end-start).microseconds / 1000
        pingop = f"█▀█ █▀█ █▄░█ █▀▀\n█▀▀ █▄█ █░▀█ █▄█\n\nϟ Arcane X System  `{ms}` ᴍs"                   
        await fuk.edit(pingop)
        await e.edit(pingop)
@bot.on(events.NewMessage(incoming=True, pattern="/arcane"))
async def info(event):
    user = event.sender_id 
    msg = await event.reply("Taking a look on Fanclub Server.")
    time.sleep(1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(1)
    await msg.edit("Initialising ◾️▫️◾️")
    time.sleep(1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(1)
    await msg.edit("Initialising ◾️▫️◾️")
    time.sleep(1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(1)
    await msg.edit("Initialising ◾️▫️◾️")
    time.sleep(1)
    await msg.edit("Initialising ▫️◾️▫️")
    time.sleep(1)
    await msg.edit("Connection successful!")
    time.sleep(2)
    if user == {OWNER_ID} or 5001573230:
         await msg.edit("Connection successful!\n\nWelcome To Arcane X System\n\nYou are a Valid User!\n\n𝐑𝐚𝐧𝐤- 𝑶𝒘𝒏𝒆𝒓")
    elif user in SUDOERS:
        await msg.edit("Connection successful!\n\nWelcome To Arcane X System\n\nYou are a Valid User!\n\n𝐑𝐚𝐧𝐤-𝗔𝗿𝗰𝗮𝗻𝗲 𝗫 𝗦𝘂𝗽𝗽𝗼𝗿𝘁𝗲𝗿!")
    else:
        await msg.edit("Chla ja ")
                   


bot_username="@VexanaMusicR0Bot"
edit_time = 1
axel1 = "https://telegra.ph/file/738e1b93e2abdbe7e459c.jpg"
axel2 = "https://telegra.ph/file/738e1b93e2abdbe7e459c.jpg"
axel3 = "https://telegra.ph/file/738e1b93e2abdbe7e459c.jpg"
axel4 = "https://telegra.ph/file/738e1b93e2abdbe7e459c.jpg"

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def proboyx(event):
  button = [[custom.Button.inline("CHECK",data="information")],[Button.url("Owner", url="https://t.me/axel_0p")],[Button.url("Support",url="https://t.me/vexana_Support")]]
  on = await bot.send_message(event.chat, f"**🔵 𝓗𝓮𝓵𝓵𝓸  {(event.sender.first_name)}**\n\n**🔵 Myself [ArcaneXsysteam](https://t.me/{bot_username})**\n**🔵 Cʀᴇᴀᴛᴇᴅ Bʏ [Axel](t.me/Axel_0p)**", file=axel1, buttons=button)
  await asyncio.sleep(edit_time)
  ok = await event.msg.edit(event.chat_id, on, file=axel2, buttons=button) 

  await asyncio.sleep(edit_time)
  ok2 = await event.msg.edit(event.chat_id, ok, file=axel3, buttons=button)

  await asyncio.sleep(edit_time)
  ok3 = await event.msg.edit(event.chat_id, ok2, file=axel1, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok4 = await event.msg.edit(event.chat_id, ok3, file=axel3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok5 = await event.msg.edit(event.chat_id, ok4, file=axel2, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok6 = await event.msg.edit(event.chat_id, ok5, file=axel3, buttons=button)
    
  await asyncio.sleep(edit_time)
  ok7 = await event.msg.edit(event.chat_id, ok6, file=axel1, buttons=button)

@bot.on(events.callbackquery.CallbackQuery(data=re.compile(b"information")))
async def callback_query_handler(event):
  try:
    boy = event.sender_id
    no = await bot.get_entity(boy)
    Axel = "Detail Featched from FanClub Server as follow \n"
    Axel += f"FIRST NAME : {no.first_name} \n"
    Axel += f"LAST NAME : {no.last_name}\n"
    Axel += f"YOU BOT : {no.bot} \n"
    Axel += f"RESTRICTED : {no.restricted} \n"
    Axel += f"USER ID : {boy}\n"
    Axel += f"USERNAME : {no.username}\n"
    await event.answer(Axel, alert=True)
  except Exception as e:
    await event.reply(f"{e}")
@bot.on(events.NewMessage(incoming=True, pattern="/help"))
async def axel(event):
        await event.reply(" Welcome help sectoin of Arcane X System",
                    buttons=[
                        [Button.url("Owner", url="https://t.me/axel_0p")],
                        [Button.url("Support",url="https://t.me/vexana_Support")]
                    ])  

@bot.on(events.NewMessage)
def my_event_handler(event):
    if 'help' in event.raw_text:
        event.reply('Type /arcane to check your status\n\n Type /info to check your Staus\n\n Type /ping to Know thae System Stats')

@bot.on(events.NewMessage(incoming=True, from_users=SUDOERS, pattern="^/sudo$"))
async def all_auths(event):
    msg = "**List of sudo users**:\n\n"
    for i in OWNER_ID:
        msg += "[{}](tg://user?id={})\n".format(i, i)
    if len(msg) > 4096:
        with open("sudo.txt", "w") as f:
            f.write(msg.replace("*", ""))
        await event.reply("**sudo users**", file="sudo.txt")
        os.remove("sudo.txt")
    else:
        await event.reply(msg)    


@bot.on(events.NewMessage(incoming=True, from_users=OWNER_ID, pattern="^/broadcast ?(.*)"))
async def broad(e):
    msg = e.pattern_match.group(1)
    if not msg:
        return await e.reply("Please use `/broadcast a_message_here`")
    xx = await e.reply("In progress...")
    done = error = 0
    for i in SUDOERS:
        try:
            await bot.send_message(int(i), msg)
            done += 1
        except:
            error += 1
    await xx.edit("Broadcast completed.\nSuccess: {}\nFailed: {}".format(done, error))        

print("\n\nBot has started thanks to @Vexana_Support")

if len(sys.argv) not in (1, 3, 4):
    try:
        bot.disconnect()
    except Exception as e:
        pass
else:
    try:
        bot.run_until_disconnected()

    except :
        pass                 
