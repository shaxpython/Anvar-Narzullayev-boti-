from aiogram import Router, F
from aiogram.types import Message,CallbackQuery,chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import Command,CommandStart
from keyboards.keyboards import start_menu
from keyboards.keyboards import tugma_holati_pashtu1
from keyboards.keyboards import you_tube_inline
from loader import bot

menu_router: Router = Router()



@menu_router.callback_query(F.data == "you_t")
async def inline_tugma_you_t(query: CallbackQuery):
    await bot.send_message(chat_id=query.from_user.id,text="https://www.youtube.com/@ibratfarzandlari")




@menu_router.message(F.text == "Pashtu tili 🇦🇫")
async def menu_tugma(msg: Message):
    await msg.answer("Pashtu tili darsliklari 🇦🇫📚",reply_markup=tugma_holati_pashtu1)

@menu_router.message(F.text == "🔙 Orqaga")
async def asosiy_menu(msg: Message):
    await msg.answer("Asosiy menyu ochildi!!",reply_markup=start_menu)


   