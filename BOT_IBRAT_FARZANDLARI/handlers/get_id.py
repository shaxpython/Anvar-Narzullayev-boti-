from aiogram import Router, F
from aiogram.types import Message, chat_member_updated
from aiogram.types.chat_member import ChatMember
from aiogram.filters import Command,CommandStart
from keyboards.keyboards import start_menu

id_router: Router = Router()



@id_router.message()
async def get_id(messaga: Message):
    file_id = messaga.video.file_id
    await messaga.reply(file_id)