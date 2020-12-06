import asyncio

from telethon import errors, functions
from telethon.tl.types import (InputMessagesFilterDocument,
                               InputPrivacyValueAllowUsers,
                               MessageMediaDocument)
from telethon.tl.types.help import UserInfo

from uniborg.util import admin_cmd, progress


@borg.on(admin_cmd(pattern="ist"))
async def test(event):
    j = await event.edit("`Bekle işlem yapılıyor 6 aylık mısın :)`")
    msg = ""
    channel1 = -1001285905728
    stats1 = await event.client.get_stats(channel1)
    onceki1 = stats1.followers.previous
    # print(f"kanal 1 onceki kullanıcı sayısı {int(onceki1)} kişi")
    msg += "kanal 1 onceki kullanıcı sayısı {int(onceki1)} kişi\n"
    simdi1 = stats1.followers.current
    # print(f"kanal 1simdiki kullanıcı sayısı {int(simdi1)} kişi")
    msg += f"kanal 1simdiki kullanıcı sayısı {int(simdi1)} kişi\n"
    fark1 = simdi1 - onceki1
    # print(f"kanal 1 aradaki fark {int(fark1)} kişi")
    msg += f"kanal 1 aradaki fark {int(fark1)} kişi\n\n"

    channel2 = -1001275030556
    stats2 = await event.client.get_stats(channel2)
    onceki2 = stats2.followers.previous
    # print(f"kanal 2 onceki kullanıcı sayısı {int(onceki2)} kişi")
    msg += f"kanal 2 onceki kullanıcı sayısı {int(onceki2)} kişi\n"
    simdi2 = stats2.followers.current
    # print(f"kanal 2 simdiki kullanıcı sayısı {int(simdi2)} kişi")
    msg += f"kanal 2 simdiki kullanıcı sayısı {int(simdi2)} kişi\n"
    fark2 = simdi2 - onceki2
    # print(f"kanal 2 aradaki fark {int(fark2)} kişi")
    msg += f"kanal 2 aradaki fark {int(fark2)} kişi\n\n"

    channel3 = -1001151369031
    stats3 = await event.client.get_stats(channel3)
    onceki3 = stats3.followers.previous
    # print(f"kanal 3 onceki kullanıcı sayısı {int(onceki3)} kişi")
    msg += f"kanal 3 onceki kullanıcı sayısı {int(onceki3)} kişi\n"
    simdi3 = stats3.followers.current
    # print(f"kanal 3 simdiki kullanıcı sayısı {int(simdi3)} kişi")
    msg += f"kanal 3 simdiki kullanıcı sayısı {int(simdi3)} kişi\n"
    fark3 = simdi3 - onceki3
    # print(f"kanal 3 aradaki fark {int(fark3)} kişi")
    msg += "kanal 3 aradaki fark {int(fark3)} kişi\n\n"

    channel4 = -1001469818787
    stats4 = await event.client.get_stats(channel4)
    onceki4 = stats4.followers.previous
    # print(f"kanal 4 onceki kullanıcı sayısı {int(onceki4)} kişi")
    msg += f"kanal 4 onceki kullanıcı sayısı {int(onceki4)} kişi\n"
    simdi4 = stats4.followers.current
    # print(f"kanal 4 simdiki kullanıcı sayısı {int(simdi4)} kişi")
    msg += f"kanal 4 simdiki kullanıcı sayısı {int(simdi4)} kişi\n"
    fark4 = simdi4 - onceki4
    # print(f"kanal 4 aradaki fark {int(fark4)} kişi")
    msg += f"kanal 4 aradaki fark {int(fark4)} kişi\n"
    await j.edit(msg)
    
