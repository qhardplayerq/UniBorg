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
            "REKLAM SEÇENEKLERİMİZ:\n=========================\n20K KANAL👇\n6 saat 35 tl 3 saat ön plan sonra sabitleme\n12 saat 55tl 5 saat ön plan sonra sabitleme\n24 saat 90tl 10 saat ön plan sonra sabitleme\n\n50K KANAL👇\n6 saat 75 tl 3 saat ön plan sonra sabitleme\n12 saat 140tl 5 saat ön plan sonra sabitleme\n24 saat 250tl 10 saat ön plan sonra sabitleme\n\n220K KİTLE👇\n6 saat 120 tl 3 saat ön plan sonra sabitleme\n12 saat 200 tl 5 saat ön plan sonra sabitleme\n24 saat 350 10 saat ön plan sonra sabitleme\n========================="

        ) 
