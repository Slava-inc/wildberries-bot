import aiohttp
from config import WB_API_URL

async def get_product_info(article: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"{WB_API_URL}/nm?nm={article}") as resp:
            if resp.status == 200:
                return await resp.json()
            return None