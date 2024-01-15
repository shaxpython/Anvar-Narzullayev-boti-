from aiogram import Router,F
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram.filters import CommandStart,Command 

sent_router: Router = Router()   

@sent_router.message(F.text=="Dars 0-1📚📖")
async def send_video_hendlar(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAMtZW3Q_CK6tMOqanhpb5lrnEUaxCgAArstAAJAd5BJuZR9EsTKqP4zBA",caption="#00 Python Darslari | Kirish so'z")
    await msg.answer_video("BAACAgIAAxkBAAM4ZW3UJmdD5RKtt4cx6Qq7NsJLDJIAAsAtAAJAd5BJU-H9mp4aRVkzBA",caption="#01 Python Darslari | Brauzerda kod yozish (Repl.it)")


@sent_router.message(F.text=="Dars 2-3📚📖")
async def send_video_hendlar(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAANIZW3U6PK9zpZ0gTty_1z-0So-XAADAjoAAv--kUlUr0Nz9x-15TME",caption="#02 Python Darslari | Birinchi Dasturimiz")
    await msg.answer_video("BAACAgIAAxkBAANSZW3WHX7llYccUR7LYpruLuFX3HMAAgI6AAL_vpFJVK9Dc_cfteUzBA",caption="#03 Python Darslari | print(), Arifmetik amallar va Sinteks")


@sent_router.message(F.text=="Dars 4-5📚📖")
async def send_video_hendlar(msg: Message):
     await msg.answer_video("BAACAgIAAxkBAANZZW3W7zmVQMlbiPH6N-gewNm23uEAAgc6AAL_vpFJdwjny980rvkzBA",caption="#04 Python Darslari | O'zgaruvchilar (Variables)")
     await msg.answer_video("BAACAgIAAxkBAANcZW3XMWz1JTEqoYX47cSpGFjYFVoAAgg6AAL_vpFJYpHZ8msbmPYzBA",caption="#05 Python Darslari | Matn bilan ishlash (Strings)")

 
@sent_router.message(F.text=="Dars 6-7📚📖")
async def send_video_hendlar(msg: Message):
     await msg.answer_video("BAACAgIAAxkBAAOAZW3Zkgz3fO-Yq_3h0dbgWUmon1sAAhE6AAL_vpFJmh-BVuckwLozBA",caption="#06 Python Darslari | Sonlar bilan ishlash")
     await msg.answer_video("BAACAgIAAxkBAAOCZW3Z1I-w1DfhxVt6txPwOyyV6mcAAuc9AAJAd4hJBInOZtisv10zBA",caption="#07 Python Darslari | Lists (Ro'yxatlar)")


@sent_router.message(F.text=="Dars 8-9📚📖")
async def send_video_hendlar(msg: Message):
     await msg.answer_video("BAACAgIAAxkBAAOgZW3xGsmeii_sU2kbB7JLp-en4kwAAhM6AAL_vpFJxyv-brQ2egszBA",caption="#08 Python Darslari | Ro'yxat bilan ishlash. O'zgarmas ro'yxatlar (Tuples)")
     await msg.answer_video("BAACAgIAAxkBAAOiZW3xU9uqmuCrC1kyqaAhIIDpSO0AAhU6AAL_vpFJNJngeTNANkYzBA",caption="#09 Python Darslari | for tsikli bilan tanishamiz")


@sent_router.message(F.text=="Dars 10📚📖")
async def send_video_hendlar(msg: Message):
     await msg.answer_video("BAACAgIAAxkBAAOkZW3xsAjJ7qsTR4iMn6byr3goGtIAAhk6AAL_vpFJw94mnzGktX8zBA",caption="#10 Python Darslari | if-else shartlari va tarmoqlanish")


















# @sent_router.message(F.text=="")
# async def send_video_hendlar(msg: Message):
#     await msg.answer_video("",caption="")
#     await msg.answer_video("",caption="")



