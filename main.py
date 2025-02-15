import asyncio
import logging
import sys

import EventsKeyborads
import env

from aiogram import Bot, Dispatcher, html
from aiogram import F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, CallbackQuery

import keyboards as kb
import EventsMessages

TOKEN = env.TELEGRAM_TOKEN
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=kb.startMenu)


@dp.message()
async def echo_handler(message: Message) -> None:
    try: await EventsMessages.get_message(message)
    except TypeError: await message.answer("Nice try!")


@dp.callback_query(F.data)
async def process_buttons_press(callback: CallbackQuery):
    try: await EventsKeyborads.get_keyboard(callback)
    except TypeError: await callback.message.answer("error button")



async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())