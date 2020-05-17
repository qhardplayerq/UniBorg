import logging

from telethon import events, functions, types
from telethon.sync import TelegramClient
import asyncio
from sample_config import Config
from uniborg.util import admin_cmd

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)

@borg.on(admin_cmd(pattern=("sil ?(.*)"))) # pylint:disable=E0602
async def _(event):
    chat = await event.get_chat()
    print(chat.id)
    await event.client.delete_dialog(chat.id)
    # await event.client.delete_dialog(user, revoke=True)


@borg.on(admin_cmd(pattern=("gonder ?(.*)"))) # pylint:disable=E0602
async def _(event):
    await event.delete()
    me = await event.client.get_me()
    input_str = event.pattern_match.group(1)
    idler = []
    async for dialog in event.client.iter_dialogs(limit=None):
        if dialog.is_user and not dialog.entity.bot and not dialog.entity.deleted:
            idler.append(dialog.entity.id)
            # print(dialog.entity.id,dialog.name)
            # print("")
            # print()
    idler.remove(me.id)
    try:
        for k in range(len(idler)):
            await event.client.send_message(
                entity=idler[k],
                message=input_str
            )
            await asyncio.sleep(3.1)
    finally:
        await event.client.send_message(
            'me',
            'herkese mesaj atıldı.'
        )


@borg.on(admin_cmd(pattern="send ?(.*)"))
@errors_handler
async def _(event):
    await event.delete()
    me = await event.client.get_me()
    idler = []
    msg = await event.get_reply_message()
    async for dialog in event.client.iter_dialogs(limit=None):
        if dialog.is_user and not dialog.entity.bot and not dialog.entity.deleted:
            idler.append(dialog.entity.id)
    idler.remove(me.id)
    try:
        for k in range(len(idler)):
            if msg:
                await event.client.forward_messages(
                    entity=idler[k],
                    messages=msg,
                    silent=True
                )
            await asyncio.sleep(3.1)
    finally:
        await event.client.send_message(
            'me',
            'herkese mesaj atıldı.'
        )
    


   
    