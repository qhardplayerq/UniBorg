# (c) @UniBorg
# Original written by @UniBorg edit by @INF1N17Y

from telethon import events
import asyncio
from collections import deque
from uniborg.util import admin_cmd
import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

@borg.on(events.NewMessage(pattern=r"\.hacklemek", outgoing=True))
async def _(event):
	if event.fwd_from:
		return
	deq = deque(list("0111011010011010111010100010010101011110010\0111011010011010111010100010010101011110010\0111011010011010111010100010010101011110010"))
	for _ in range(100):
		await asyncio.sleep(1)
		await event.edit("".join(deq))
		deq.rotate(1)
		
@borg.on(admin_cmd(pattern="elegecir", outgoing=True))
async def bkallp(event):
    a = "❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 💔 💘 💝".split(" ")
    d = await event.reply("...")
    for t in a:
        await d.edit(t)
        await asyncio.sleep(5)
