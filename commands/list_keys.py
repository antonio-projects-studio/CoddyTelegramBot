from aiogram.types import Message

from database import my_data


async def list_keys(message: Message):
    forward_message: str = ', '.join(my_data.list_keys())
    if forward_message is '':
        forward_message = "В вашей базе нет данных"
    await message.answer(forward_message)
