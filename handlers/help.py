from aiogram import Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

def register_help(dp: Dispatcher):
    @dp.message(Command("help"))
    async def help(message: Message):
        await message.answer(
            "ℹ Чтобы мы с вами связались, нужно заполнить заявку через /application 📋.\n\n"
            "☎ Если не хотите ждать:\n"
            "📱 +998 95 145 21 21\n"
            "🌐 Наш сайт: www.globaleducation.uz/\n"
            "📸 Instagram: Globaleducation.uz\n"
            "💬 Telegram: @globaleducation_msg"
        )
