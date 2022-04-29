from aiogram import types
from dispatcher import dp

@dp.message_handler(content_types=types.ContentTypes.ANY)
async def all_other_messages(message: types.Message):
    await message.reply("Этот бот принимает только текстовые сообщения!")