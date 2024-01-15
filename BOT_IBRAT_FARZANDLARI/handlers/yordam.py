from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import Command,CommandStart
from keyboards.keyboards import start_menu

help_router: Router = Router()



@help_router.message(Command("help"))
async def help(message: Message):
    await message.answer(f"""Salom {message.from_user.full_name}!!\n
Siz agar bu botga til o'raganish uchun kirgan bo'lsangiz adashmabsiz😀🤓\n

«Ibrat Farzandlari» bilan xorijiy tillarni mutlaqo bepul, oson va kreativ usulda oʻrganamiz
🇺🇿🇬🇧🇷🇺🇹🇷🇸🇦🇪🇸🇮🇹🇩🇪🇫🇷🇨🇳🇯🇵🇰🇷🇮🇳

Agarsiz hozir shu yerni o'zida bironta tilni o'rgan modchi bo'lsangiz pastdagi tugmalarni bosing🔝

agar meni trafikim ko'p you tube dan o'rganaman desangiz you tubeda ham sahifamiz bor 1429631965 padda


""")