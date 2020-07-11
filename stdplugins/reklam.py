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
            "1-)Kanal: https://t.me/joinchat/AAAAAEylXUB6ztFxdgHp1w \n2-)Kanal: t.me/deryanin_linkleri \n3-)Kanal: t.me/linkteskilati3 \n4-)Grup: t.me/deryanin_mekani \n56-)Grup: https://t.me/joinchat/PrW4fBcmiV-qpqdtBwdYsQ"

        ) 