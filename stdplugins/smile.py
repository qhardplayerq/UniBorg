﻿# (c) @UniBorg
# Original written by @UniBorg edit by @INF1N17Y

import asyncio
import logging
from collections import deque

from telethon import events

from uniborg.util import admin_cmd

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


@borg.on(events.NewMessage(pattern=r"\.smile", outgoing=True))
async def _(event):
  await event.delete()
    if event.fwd_from:
        return
    deq = deque(list("😃😄😁😆😅😂🤣🙃"))
    for _ in range(100):
        await asyncio.sleep(0.1)
        await event.edit("".join(deq))
        deq.rotate(1)


@borg.on(admin_cmd(pattern="bsmile", outgoing=True))
async def bkallp(event):
  await event.delete()
    a = "😃 😄 😁 😆 😅 😂 🤣 🙃".split(" ")
    d = await event.reply("...")
    for t in a:
        await d.edit(t)
        await asyncio.sleep(5)
