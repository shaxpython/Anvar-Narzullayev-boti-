from aiogram import Router,F
from aiogram.types import Message,CallbackQuery,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove,InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.filters import CommandStart,Command
from loader import bot

menu_router: Router = Router()



@menu_router.callback_query(F.data=="Birinchi")
async def menu_inline(query: CallbackQuery):
    menu = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text="Darslar📚📚📖",callback_data="Darslar📚📚📖")
            ]
        ]
    )
    await bot.send_message(chat_id=query.from_user.id,text="""Salom Agar Siz Men Haqimda Bilmoqchi Bo'l Sangiz Adash Mab Siz😃😃!\n
Mendan Python Dasturlash Tili Bo'yicha Chiqarilgan Videolarni Ko'rishingiz Mumkin😎😎\n
Yoki  Websitetimizga Kirib Darslarni📖📖 Ko'rishingiz Mumkin🤩🤩\n
Websatemizda Esa Anvar Narzullayevdan Haqiqiy Pullikdarslar O'rganishingiz Mumkin🤩🤯😮\n
Video Darslarni Kurish Uchun Pastdagi Tugmani Bosing🔝✅\n
⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️ ⬇️          
""",reply_markup=menu)


@menu_router.callback_query(F.data=="Darslar📚📚📖")
async def menu_henlar(query: CallbackQuery):
    menu2 = ReplyKeyboardMarkup(
        keyboard=[
             [
                 KeyboardButton( text="Bepul Darslar")
             ],
             [
                 KeyboardButton(text="Websitega Utish")
             ],
         ],
        resize_keyboard =  True
    )
    await bot.send_message(chat_id=query.from_user.id,text="Darslar Tugmalari Ochildi!!",reply_markup=menu2)





@menu_router.message(F.text=="Bepul Darslar")
async def  dars_henler(msg: Message):
    menu  = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton(text="Dars 0-1📚📖"),
                KeyboardButton(text="Dars 2-3📚📖")
            ],
            [
                KeyboardButton(text="Dars 4-5📚📖"),
                KeyboardButton(text="Dars 6-7📚📖")
            ],
            [
                KeyboardButton(text="Dars 8-9📚📖"),
                KeyboardButton(text="Dars 10📚📖"),
            ],
            [
                KeyboardButton(text="🔝 Asosiy Menyu")
            ],
        ],
        resize_keyboard=True
    )
    await msg.answer("Darslar📚📖 menusi!!",reply_markup=menu)
    

@menu_router.message(F.text=="🔝 Asosiy Menyu")
async def  start(message: Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton( text="Bepul Darslar")
            ],
            [
                KeyboardButton(text="Websitega Utish")
            ],
        ],
        resize_keyboard =  True
    )
    await message.answer("Asosiy Menyuga Utildi!!",reply_markup = menu)

@menu_router.message(F.text=="Websitega Utish")
async def  start(message: Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton( text="Biznning Websaytimiz")
            ],
            [
                KeyboardButton(text="🚫Bekor Qilish🚫")
            ],
        ],
        resize_keyboard =  True
    )
    await message.answer("Websitedagi Darslarni Kuring!!",reply_markup = menu)




@menu_router.message(F.text=="Biznning Websaytimiz")
async def web_qilish(msg: Message):
    await msg.reply("Website  https://python.sariq.dev/")


@menu_router.message(F.text=="🚫Bekor Qilish🚫")
async def bekor_key(msg: Message):
    menu = ReplyKeyboardMarkup(
        keyboard=[
            [
                KeyboardButton( text="Bepul Darslar")
            ],
            [
                KeyboardButton(text="Websitega O'tish")
            ],
        ],
        resize_keyboard =  True
    )
    await msg.answer("Asosiy Menyuga o'tildi!!",reply_markup = menu)


    