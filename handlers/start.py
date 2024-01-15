from aiogram import Router
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,CallbackQuery,ReplyKeyboardRemove,InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.filters import CommandStart,Command
from loader   import bot

start_router: Router = Router()   

@start_router.message(CommandStart())
async def start_com(msg: Message):
    menu = InlineKeyboardMarkup(
        inline_keyboard =[
            [
                InlineKeyboardButton(text="Malumotlar🧑🏻‍💻",callback_data="Birinchi")
            ],
        ]
    )
    await msg.answer("""Salom Men Anvar Narzullayevning Botiman Man😎🤚\n
Agar Siz Men Haqimda Malumot Olmoqchi Bo'lsangiz😃\n
\n
Pastdagi Tugmani Bosing🔝✅\n
⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️  \n
 """,reply_markup=menu)




    #