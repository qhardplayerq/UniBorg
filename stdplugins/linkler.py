import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="link"))
async def _(event):
    await event.delete()
    for a in range(1,11):
        await borg.send_message(
            event.chat_id,
            "Kanal: t.me/bayanlink "+
            "Grup: t.me/deryanin_mekani"

        )