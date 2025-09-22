from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

def register_start(dp: Dispatcher):
    @dp.message(Command("start"))
    async def start(message: Message):
        await message.answer(
            "👋 Добро пожаловать в *Global Education.uz*!\n\n"
            "Хотите учиться за границей? 🌍\n"
            "📌 Запишитесь на *бесплатную консультацию* через /application",
            parse_mode="Markdown"
        )
