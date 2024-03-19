from aiogram.filters import CommandStart
from aiogram.types import Message
from aiogram.utils.markdown import hbold
from aiogram.enums import parse_mode
from bot.dispatcher import dp
from aiogram.utils.i18n import lazy_gettext as _
from bot.dispatcher import *


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {hbold(message.from_user.full_name)}!" , parse_mode='HTML')
