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
	deq = deque(list("10001110101010010111001101000101010111010101001011100110100010101011101010100101110011010001010101110111010010100100101010010100100110001001010010110101010010111001101000101010111010101001011100110100010101011101010100101110011010001010101110111010011101010100101110011010001010101110101010010111001101000101010111010101001011100110100010101011010101001011100110100010101011101010100101110011010001010101110101010010111001101000101010111011101001010010010101001010010011000100101001001010010010011101110100101001001010100101001001100010010100100101001001000100100101010010100100110001001010010010100100100010100100100010101110101010010111001101000101010111010101001011100110100010101011101010100101110011010001010101110111010010100100101010010100100110001001010010010100100100010101010010111001101000101010111010101001011100110101010111011010011010111010100010010101011110010010010000100"))
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
