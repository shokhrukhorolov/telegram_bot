from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

def register_application(dp: Dispatcher):
    @dp.message(Command("application"))
    async def application(message: Message):
        await message.answer("📋 Начинаем заполнение заявки (здесь будет анкета).")
