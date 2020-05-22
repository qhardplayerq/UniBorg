import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="reklam"))
async def _(event):
    await event.delete()
    for a in range(1,2):
        await borg.send_message(
            event.chat_id,
            "1-)5K Kanal: t.me/linkteskilati3\n\n2-)5.1K Kanal: t.me/bayanlink\n\n3-)15K Grup: t.me/deryanin_mekani"

        ) 