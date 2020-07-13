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
	deq = deque(list("1101001001010101001111101001001\n1111000110010110000111001001011\n0001001110010101011000110111101\n1111000001010101011101001000000\n0010011101100111101110011010001\n0110010100101001001010001010000\n0100100111010101011101010010010\n1100100100101010101110100100001\n1000010011110010111001010110010\n1101001001010101011101001001001\n000101000101010010010101001010111011\n0000100111001111111110010101001\n0000101111001000000010100010001\n1111010011100101001110011011011\n1001100111100001010011110011011\n1110010110000001101000111010101"))
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
