import json
import logging
import requests
# import aiohttp
import asyncio
from uniborg.util import admin_cmd
from urllib.request import Request, urlopen
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)
logger = logging.getLogger(__name__)



@borg.on(admin_cmd(pattern=("kisalt ?(.*)")))
async def get_adzan(event):
  link = event.pattern_match.group(1)
  if link:
      api = f"https://ay.link/api/?api=e2bb35a996ea8c9dfa4e5011005730bb584e283f&url={link}&alias&ct=1"
      req = Request(api, headers={'User-Agent': 'Mozilla/5.0'})
      web_byte = urlopen(req).read()
      webpage = web_byte.decode('utf-8')
      data = json.loads(webpage)
      await event.edit(data['shortenedUrl'])







        
        
