import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

TOKEN = ('8256805328:AAFVX32vd17WOs2ddtQoIvEfRFQ6F95aNio')
CHANNEL_ID = '-1003081059373'

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())