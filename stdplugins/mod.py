import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="moderator"))
async def _(event):
    await event.delete()
    for a in range(1,2):
        await borg.send_message(
            event.chat_id,
            "1: https://t.me/joinchat/AAAAAEylXUB6ztFxdgHp1w\n2: https://t.me/joinchat/AAAAAEv_bBx6bl0AEojIJA\n3: https://t.me/joinchat/AAAAAESgf0f1wctsKPJ0cg\n4: https://t.me/joinchat/AAAAAFebp6PIGgUeAC8DWA"

        ) 
