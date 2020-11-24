import json
import logging
import requests
import aiohttp
import asyncio
from uniborg.util import admin_cmd

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)



@borg.on(admin_cmd(pattern=("kisalt ?(.*)")))
async def get_adzan(event):
    
    link = event.pattern_match.group(1)
    if link:
        api = f"https://ay.link/api/?api=e2bb35a996ea8c9dfa4e5011005730bb584e283f&url={link}&alias&ct=1"
        async with aiohttp.ClientSession() as session:
          async with session.get(api) as response:
            ilk = await response.json()
            kk = json.loads(ilk)
            son = kk['shortenedUrl']
            await event.edit("Link👉 {}".format(son))


        
        
