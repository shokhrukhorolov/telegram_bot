import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode

TOKEN = ('')
CHANNEL_ID = ''

logging.basicConfig(level=logging.INFO)

bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
