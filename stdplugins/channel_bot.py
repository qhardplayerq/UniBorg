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
                    

@borg.on(admin_cmd(pattern=r"ch ?(.*)",allow_sudo=True))
async def get_media(event):
    chat = "https://t.me/joinchat/AAAAAEylXUB6ztFxdgHp1w"
    from_chat = "https://t.me/joinchat/AAAAAEylXUB6ztFxdgHp1w"
    mesajlar = []
    print("kanaldan rastgele mesaj seçiliyor.")
    await event.edit("kanaldan rastgele link seçiliyor.")
    async for message in borg.iter_messages(chat):
        mesajlar.append(message.id)

    secim = int(random.choice(mesajlar))
    print(secim)
    x = await borg.forward_messages(
        entity=chat,
        messages=secim,
        from_peer=chat
    )
    await event.edit("kanala başarılı bir şekilde link gönderildi. Kontrol etmek için @bayanlink")
    # x = await borg.get_messages(chat, s)
    print(x)