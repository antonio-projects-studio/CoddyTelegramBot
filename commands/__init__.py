from aiogram.filters import CommandStart, Command 
from aiogram.types import BotCommand

from config import dp

from .start import *
from .upload import *
from .load import *
from .delete import *
from .list_keys import *

dp.message.register(start, CommandStart())
dp.message.register(upload, Command(commands='upload'))
dp.message.register(load, Command(commands='load'))
dp.message.register(delete, Command(commands='delete'))
dp.message.register(list_keys, Command(commands='list_keys'))

bot_commands = [
    BotCommand(command='start', description='начало'),
    BotCommand(command='upload', description='загрузка данных в базу'),
    BotCommand(command='load', description='получить данные'),
    BotCommand(command='delete', description='удалить данные'),
    BotCommand(command='list_keys', description='получить список ключей')
]
