"""Shouts a message in MEME way
usage: .shout message
originaly from : @corsicanu_bot
"""
import logging

from telethon import events

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)


@borg.on(events.NewMessage(pattern=r"\.shout", outgoing=True)) # pylint:disable=E0602
async def shout(args):
    if args.fwd_from:
        return
    else:
        msg = "```"
        messagestr = args.text
        messagestr = messagestr[7:]
        text = " ".join(messagestr)
        result = []
        result.append(' '.join(s for s in text))
        for pos, symbol in enumerate(text[1:]):
            result.append(symbol + ' ' + '  ' * pos + symbol)
        result = list("\n".join(result))
        result[0] = text[0]
        result = "".join(result)
        msg = "\n" + result
        await args.edit("`"+msg+"`")
