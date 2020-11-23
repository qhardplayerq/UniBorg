import logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd

@borg.on(admin_cmd(pattern="linkler"))
async def _(event):
    await event.delete()
    for a in range(1,2):
        await borg.send_message(
            event.chat_id,
            "=====================KANALLARIMIZ=====================\n1: https://t.me/joinchat/AAAAAEylXUB6ztFxdgHp1w \n2: https://t.me/deryanin_linkleri\n3: https://t.me/joinchat/AAAAAEv_bBx6bl0AEojIJA \n4: https://t.me/joinchat/AAAAAESgf0f1wctsKPJ0cg \n5: https://t.me/joinchat/AAAAAE_oUYlNq2c45oQRlQ\n6: https://t.me/joinchat/AAAAAFebp6PIGgUeAC8DWA\n7: https://t.me/joinchat/AAAAAE9kOnXSwSOitjpjJA\n8: https://t.me/joinchat/AAAAAFO7l8-6EIxXJsRHkg\n9: https://t.me/joinchat/AAAAAEzIWLtq3-pUg9G9fA\n10: https://t.me/joinchat/AAAAAEUnlnmhE4z26NdxvQ\n11: https://t.me/joinchat/AAAAAFehN1YfV3UYs0YsRw \n12: https://t.me/joinchat/AAAAAFgeWypj9goHR6g6bg      \n \n==================SOHBET GRUPLARIMIZ==================\n1: https://t.me/deryanin_mekani \n2: https://t.me/joinchat/PrW4fBcmiV-qpqdtBwdYsQ\n3: https://t.me/joinchat/PrW4fE99MRNqBiUYBKUXLw\n\n==================VİDEO KANALLARIMIZ==================\n1: https://t.me/joinchat/AAAAAFeV963Az-qZVyFvig"

        ) 
