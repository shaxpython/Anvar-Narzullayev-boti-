from aiogram import Router
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton,ReplyKeyboardRemove
from aiogram.filters import CommandStart 

get_router: Router = Router()

@get_router.message()
async  def  get_hendler(msg: Message):
    file_id = msg.video.file_id
    await msg.reply(file_id)
