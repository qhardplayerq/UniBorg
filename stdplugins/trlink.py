import json
import logging

import requests

from uniborg.util import admin_cmd

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(name)



@borg.on(admin_cmd(pattern=("kisalt ?(.*)")))
async def get_adzan(event):
    
    link = event.pattern_match.group(1)
    if link:
        api = f"https://ay.link/api/?api=e2bb35a996ea8c9dfa4e5011005730bb584e283f&url={link}&alias&ct=1"
        #api_2 = f"http://pubiza.com/api.php?token=snmmRSSLfiZQUGmfZox6k3UjQPEZpLa8&url={link}"
        r = requests.get(api)
        #r_2 = requests.get(api_2)
        #kisa_link_2 = r_2.text
        kisa_link = r.json()['shortenedUrl']
        await event.edit("Link👉 {}\n\n📌Reklam Geçmek için👇\n👉 @linkk_gecmee".format(kisa_lin,kisa_link_2))
