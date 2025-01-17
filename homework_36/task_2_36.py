import asyncio
import aiohttp
import json

from aiohttp import ClientSession


async def get_inf():
    async with ClientSession() as session:
        url = 'https://api.nasa.gov/planetary/apod'
        key = 'OdRW9eU7kggJmrc8pOQVxQtpV7lUZvjNlFkgjbL'
        date = '2024-02-24'
        params = {'api_key': key,
                  'date': date,
                  'hd': 'True'
                  }
        async with session.get(url=url, params=params) as response:
            nasa_inf = await response.json()
            return nasa_inf

async def main():
    tasks = [asyncio.create_task(get_inf())]
    res = await asyncio.gather(*tasks)
    with open('homework.json', 'w') as outfile:
        json.dump(res, outfile)

asyncio.run(main())
