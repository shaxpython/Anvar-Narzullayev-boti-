from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import Command,CommandStart
from keyboards.keyboards import start_menu
from keyboards.keyboards import you_tube_inline

start_router: Router = Router()

@start_router.message(Command('start'))
async def start(message: Message):
    await message.answer(f"Assalomu alaykum {message.from_user.full_name}\n \nAgar siz biz haqimizda malumot olmoqchi bo'lasan?\n giz /help ni ustiga bosing ",reply_markup=start_menu)
    await message.answer("Bizni kanallarimiz 🔝🔝🔝",reply_markup=you_tube_inline)