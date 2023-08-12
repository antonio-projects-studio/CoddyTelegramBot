import logging
import os
import sys
file_path = os.path.realpath(__file__)
# Получение директории, в которой находится файл скрипта
script_dir = os.path.dirname(file_path)
sys.path.append(script_dir)

from aiogram.types import BotCommandScopeDefault
import asyncio

from database import *
from config import *
from commands import *


async def main():
    await bot.set_my_commands(bot_commands, scope=BotCommandScopeDefault())
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


logging.basicConfig(level=logging.DEBUG)
try:
    asyncio.run(main())
finally:
    my_data.upload()
    print(1)

