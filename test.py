from search import *
import asyncio
from bs4 import BeautifulSoup as soup
from urllib.request import urlope as uReq

async def test_URL():
    search = (search_google("Who is Salman Khan", 10))
    print(search)

async def main():
    asyncio.gather(test_URL())

if __name__ == "__main__":
    asyncio.run(main())
