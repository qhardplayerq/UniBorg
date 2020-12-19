import json
import logging
import requests
# import aiohttp
import asyncio
from uniborg.util import admin_cmd
import urllib.request 
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)



@borg.on(admin_cmd(pattern=("kisalt ?(.*)")))
async def get_adzan(event):
    
    link = event.pattern_match.group(1)
    if link:
        api = f"https://ay.link/api/?api=e2bb35a996ea8c9dfa4e5011005730bb584e283f&url={link}&alias&ct=1"
        with urllib.request.urlopen(api,headers={'Content-Type':'application/json'}) as url:
            data = json.loads(url.read().decode())
            msg = data['shortenedUrl']
            await event.edit(msg)


        
        
