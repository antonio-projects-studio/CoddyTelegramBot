from aiogram.filters import CommandObject
from aiogram.types import Message

from database import my_data


async def delete(message: Message, command: CommandObject):
    if command.args is None or len(command.args.split(' ')) != 1:
        await message.answer("Данную комманду надо использовать с одним аргументом <key>")

    else: 
        key = command.args
        my_data.delete(key)
        await message.answer(f"Данные успешно удалены")
