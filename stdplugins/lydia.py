import asyncio
import io
import logging
from time import time

import coffeehouse as cf
from coffeehouse.api import API
from coffeehouse.lydia import LydiaAI
from database.lydiadb import add_lydia, check_lydia, delete_lydia
from sample_config import Config
from uniborg.util import admin_cmd

logger = logging.getLogger(__name__)
logger.setLevel(logging.ERROR)


if Config.LYDIA_API is not None:
    api_key = Config.LYDIA_API
    # Create the CoffeeHouse API instance
    coffeehouse_api = API(api_key)
    # Create Lydia instance
    lydia = LydiaAI(coffeehouse_api)


@borg.on(admin_cmd(pattern="(ena|del|lst)cf", allow_sudo=True))
async def lydia_disable_enable(event):
    if event.fwd_from:
        return
    if Config.LYDIA_API is None:
        await event.edit("please add required `LYDIA_API` env var")
        return
    if event.reply_to_msg_id is not None:
        input_str = event.pattern_match.group(1)
        reply_msg = await event.get_reply_message()
        user_id = reply_msg.from_id
        chat_id = event.chat_id
        await event.edit("Processing...")
        if input_str == "ena":
            # Create a new chat session (Like a conversation)
            session = lydia.create_session()
            logger.info(session)
            # logger.info("Session ID: {0}".format(session.id))
            # logger.info("Session Available: {0}".format(str(session.available)))
            # logger.info("Session Language: {0}".format(str(session.language)))
            # logger.info("Session Expires: {0}".format(str(session.expires)))
            logger.info(add_lydia(user_id, chat_id,
                                  session.id, session.expires))
            await event.edit(f"Lydia AI turned on for [user](tg://user?id={user_id}) in chat: `{chat_id}`")
        elif input_str == "del":
            logger.info(delete_lydia(user_id, chat_id))
            await event.edit(f"Lydia AI turned off for [user](tg://user?id={user_id}) in chat: `{chat_id}`")
        elif input_str == "lst":
            lsts = check_lydia(event.chat_id)
            if len(lsts) > 0:
                output_str = "Lydia AI enabled users:\n\n"
                for lydia_ai in lsts:
                    output_str += f"[user](tg://user?id={lydia_ai.user_id}) in chat `{lydia_ai.chat_id}`\n"
            else:
                output_str = "no Lydia AI enabled users / chats. Start by replying `.enacf` to any user in any chat!"
            if len(output_str) > Config.MAX_MESSAGE_SIZE_LIMIT:
                with io.BytesIO(str.encode(output_str)) as out_file:
                    out_file.name = "lydia_ai.text"
                    await event.client.send_file(
                        event.chat_id,
                        out_file,
                        force_document=True,
                        allow_cache=False,
                        caption="Lydia AI enabled users",
                        reply_to=event
                    )
            else:
                await event.edit(output_str)
        else:
            await event.edit("Reply To User Message to Add / Delete them from Lydia Auto-Chat.")
    else:
        await event.edit("Reply To A User's Message to Add / Delete them from Lydia Auto-Chat.")


@borg.on(admin_cmd(incoming=True))
async def on_new_message(event):
    if event.chat_id in Config.UB_BLACK_LIST_CHAT:
        return
    if Config.LYDIA_API is None:
        return
    reply = await event.get_reply_message()
    if reply is None:
        pass
    elif reply.from_id == borg.uid:
        pass
    else:
        return
    if not event.media:
        user_id = event.from_id
        chat_id = event.chat_id
        s = get_s(user_id, chat_id)
        if s is not None:
            session_id = s.session_id
            session_expires = s.session_expires
            query = event.text
            # Check if the session is expired
            # If this method throws an exception at this point,
            # then there's an issue with the API, Auth or Server.
            if session_expires < time():
                # re-generate session
                session = lydia.create_session()
                logger.info(session)
                session_id = session.id
                session_expires = session.expires
                logger.info(
                    add_s(user_id, chat_id, session_id, session_expires))
            # Try to think a thought.
            try:
                async with event.client.action(event.chat_id, "typing"):
                    await asyncio.sleep(1)
                    output = lydia.think_thought(session_id, query)
                    await event.reply(output)
            except cf.exception.CoffeeHouseError as e:
                logger.info(str(e))
