from aiogram.filters import CommandObject
from aiogram.types import Message

from database import my_data


async def upload(message: Message, command: CommandObject):
    if command.args is None or len(command.args.split(' ')) != 2:
        await message.answer("Данную комманду надо использовать с двумя аргументами <key>, <value>")

    else: 
        key, value = command.args.split(' ')
        data_for_update = {key : value}
        my_data.update_data(data_for_update)
        await message.answer(f"Данные успешно загруженны, для того чтобы их получить используйте команду"
                             f"/load <key>")
