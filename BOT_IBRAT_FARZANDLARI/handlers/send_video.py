from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import Command,CommandStart
from keyboards.keyboards import start_menu
from keyboards.keyboards import tugma_holati_pashtu1


send_video_router: Router = Router()


@send_video_router.message(F.text == "Birinchi dars 🇦🇫📚¹")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAN5ZYQ3Qb_FHZyRCy2hglV6a7HjVyoAAt07AAK2SyBI0to5SKG_t78zBA",caption=" Pashtu tili bilan tanishuv | 1-dars | Pashtu tilini 0 dan o'rganish")
    
    


@send_video_router.message(F.text == "Ikkinchi dars 🇦🇫📚²")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAONZYQ4vrNFWXTgsiivKhAGnR0g3hEAAvg7AAK2SyBIS4yF-MTsv98zBA",caption=" Pashtu tili alifbosida harflarning talaffuzi | 2-dars | Pashtu tilini 0 dan o'rganish")


@send_video_router.message(F.text == "Uchinchi dars 🇦🇫📚³")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAOqZYQ-tSuXmKKaJlNkenwdCJvo3iMAAhE8AAK2SyBIv8pAZFnrqx0zBA",caption=" Pashtu alifbosida ا ب پ ت ټ ث harflarining yozilishi | 3-dars | Pashtu tilini 0 dan o'rganish")


@send_video_router.message(F.text == "To'rinchi dars 🇦🇫📚⁴")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAOzZYRAEgYUDZH2yRm0Vgtljc-JP24AAlA8AAK2SyBI_5pskcXiGYAzBA",caption="Pashtu alifbosida ج چ ځ څ ح خ harflarining yozilishi | 4-dars | Pashtu tilini 0 dan o'rganish")


@send_video_router.message(F.text == "Beshinchi dars 🇦🇫📚⁵")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAO9ZYRCyV3UP3yqX76BJJYeTKo7sS0AAnw8AAK2SyBIkHChDn7Qr9kzBA",caption="Harflarni ulab yozish | 5-dars | Pashtu tilini 0 dan o'rganish")


@send_video_router.message(F.text == "Oltinchi dars 🇦🇫📚⁶")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAPFZYRI3WUUiW7Ubj06d94LXxKt4G0AAus8AAK2SyBIeSftEmi4N9QzBA",caption="Pashtu alifbosidagi د ډ ذ ر ړ ز ژ ږ harflarining yozilishi | 6-dars | Pashtu tilini 0 dan o'rganish")


@send_video_router.message(F.text == "Yettinchi dars 🇦🇫📚⁷")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAPcZYRLI8jCVh9FIuRuhTYJttyF2csAAho9AAK2SyBI9UfYA7jxFRczBA",caption="Pashtu alifbosidagi س ش ښ ص ض ط ظ harflarining yozilishi | 7-dars | Pashtu tilini 0 dan o'rganish")



@send_video_router.message(F.text == "Sakkizinchi dars 🇦🇫📚⁸")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAPlZYRQt3OJwl3D2l8lhN8OxtITo2UAAlQ9AAK2SyBIa9YqwPwaKkozBA",caption="Pashtu alifbosidagi ع غ ف ق ک ګ harflarining yozilishi | 8-dars | Pashtu tilini 0 dan o'rganish")
    
    



@send_video_router.message(F.text == "To'qqizzinchi dars 🇦🇫📚⁹")
async def send_video_pashtu1_handler(msg: Message):
    await msg.answer_video("BAACAgIAAxkBAAPoZYRRPvji7hsXyiymhrFQoSI_k2gAAlo9AAK2SyBI7tBV_hHiLEAzBA",caption="Pashtu alifbosidagi ل م ن ڼ و harflarining yozilishi | 9-dars | Pashtu tilini 0 dan o'rganish")
    
    