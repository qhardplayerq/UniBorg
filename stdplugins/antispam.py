#COMBOT ANTI SPAM SYSTEM IS USED
#created for @uniborg (unfinished)

import asyncio
import logging
import os
import sys

from telethon import events
from telethon.tl.functions.channels import EditBannedRequest
#COMBOT ANTI SPAM SYSTEM IS USED
#created for @uniborg (unfinished)
from telethon.tl.types import ChatBannedRights

from sample_config import Config
from uniborg.util import admin_cmd

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

@borg.on(events.ChatAction())
async def _(cas):
    chat = await cas.get_chat()
    if (chat.admin_rights or chat.creator):
        if cas.user_joined or cas.user_added: 
            user = await cas.get_user()
            id = user.id
            mid = "{}".format(chat.title)
            mention = "[{}](tg://user?id={})".format(user.first_name, user.id) 
            from requests import get
            r = get(f'https://combot.org/api/cas/check?user_id={id}') 
            r_dict = r.json() 
            if r_dict['ok']:
                try: 
                    more = r_dict['result']
                    # rights = ChatBannedRights(
                    #     until_date=None,
                    #     view_messages=True,
                    #     send_messages=True
                    # )

                    
                    # await borg.send_message('me',entity)
                    # get_entity = await event.get_participants(chat)
                    # await borg.send_message('me',get_entity)
                    # await borg(EditBannedRequest(cas.chat_id, id, rights))
                    entity = await borg.get_entity(chat)
                    await borg.edit_permissions(int('-100' + str(entity.id)), user.id, view_messages=False)
                    await borg.send_message(Config.PRIVATE_GROUP_BOT_API_ID, "**antispam log** \n**Who**: {} \n**Where**: {} \n**How**: [here](https://combot.org/api/cas/check?user_id={}) \n**Action**: Banned \n**More**: ```{}```".format(mention, mid, id, more),link_preview=False)
                except (Exception) as exc:
                    await borg.send_message(Config.PRIVATE_GROUP_BOT_API_ID, str(exc))
                    exc_type = sys.exc_info()
                    exc_tb = sys.exc_info()
                    fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
                    print(exc_type, fname, exc_tb.tb_lineno)
                    print(exc)
                    await borg.send_message(Config.PRIVATE_GROUP_BOT_API_ID,exc)
                    await asyncio.sleep(5)
                    await borg.send_message(Config.PRIVATE_GROUP_BOT_API_ID,fname)
                    await asyncio.sleep(5)
                    await borg.send_message(Config.PRIVATE_GROUP_BOT_API_ID,exc_tb.tb_lineno)
    else:
        return ""
