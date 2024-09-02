import os
import aiohttp
import asyncio
from dotenv import load_dotenv

load_dotenv()

API_KEYS = {
    "pinnacle": os.getenv("PINNACLE_API_KEY"),
    "livescore": os.getenv("LIVESCORE_API_KEY"),
    "api_football": os.getenv("API_FOOTBALL_KEY")
}

async def fetch_data(url, headers, params=None):
    async with aiohttp.ClientSession() as session:
        async with session.get(url, headers=headers, params=params) as response:
            return await response.json()

async def fetch_all_data():
    urls = {
        "pinnacle": "<https://pinnacle-odds.p.rapidapi.com/kit/v1/special-markets>",
        "livescore": "<https://livescore6.p.rapidapi.com/v2/search>",
        "football": "<https://api-football-v1.p.rapidapi.com/v2/odds/league/865927/bookmaker/5>"
    }

    headers = {
        "pinnacle": {"x-rapidapi-key": API_KEYS["pinnacle"]},
        "livescore": {"x-rapidapi-key": API_KEYS["livescore"]},
        "football": {"x-rapidapi-key": API_KEYS["api_football"]}
    }

    tasks = [fetch_data(urls[api], headers[api]) for api in urls]
    responses = await asyncio.gather(*tasks)
    return responses

if __name__ == "__main__":
    data = asyncio.run(fetch_all_data())
    print(data)
