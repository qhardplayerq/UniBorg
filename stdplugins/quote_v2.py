import logging

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError

from uniborg.util import admin_cmd

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)


@borg.on(admin_cmd(pattern=("q ?(.*)")))
# @borg.on(outgoing=True, pattern="^.q(?: |$)(.*)")
async def _(event):
    if event.fwd_from:
        return
    if not event.reply_to_msg_id:
        await event.edit("```Reply to any user message.```")
        return
    reply_message = await event.get_reply_message()
    if not reply_message.text:
        await event.edit("```Reply to text message```")
        return
    chat = "@QuotLyBot"
    sender = reply_message.sender
    if reply_message.sender.bot:
        await event.edit("```Reply to actual users message.```")
        return
    await event.edit("```Making Love```")
    async with borg.conversation(chat) as conv:
        try:
            response = conv.wait_event(events.NewMessage(
                incoming=True, from_users=1031952739))
            await borg.forward_messages(chat, reply_message)
            response = await response
        except YouBlockedUserError:
            await event.reply("```Please unblock @QuotLyBot and try again```")
            return
        if response.text.startswith("Hi!"):
            await event.edit("```Can you kindly disable your forward privacy settings for good?```")
        else:
            await event.delete()
            # await borg.forward_messages(event.chat_id, response.message)
            await event.client.send_message(
                entity=event.chat_id,
                message=response.message,
                reply_to=event.message.id,
                # # parse_mode="html",
                # link_preview=False,
                # # file=message_media,
                # silent=True
            )
