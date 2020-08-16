import asyncio
import logging
import os
import random
import subprocess
import sys
import time

from telethon import events
from telethon.errors import FloodWaitError
from telethon.tl import functions

from sample_config import Config
from uniborg.util import admin_cmd, humanbytes, progress, time_formatter

DEL_TIME_OUT = 3
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
                    
@borg.on(admin_cmd(pattern="video ?(.*)",allow_sudo=True))
async def get_media(event):
    reply_message = await event.get_reply_message()
    k = await event.edit("post gönderiliyor...")
    # print(reply_message)
    if reply_message:
        await asyncio.sleep(1.2)
        await event.client.send_message(
            entity=await event.client.get_entity("@linkteskilati3"),
            message=reply_message
        )
        await asyncio.sleep(1.2)

        
        # await event.reply(reply_message)
    else:
        await k.edit("mesajı yanıtla lan :)")
#     await k.edit("mesaj tüm kanallara gönderildi")
       
       
        
