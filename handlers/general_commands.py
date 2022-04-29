from aiogram import types
from config import MAX_RESULTS_NUMBER
from dispatcher import dp

from .proverbs_functions import get_proverbs


@dp.message_handler(commands=['start', 'help'])
async def help(message: types.Message):
    await message.answer("Введите ключевые слова через запятую или пробел")


@dp.message_handler(content_types=types.ContentTypes.TEXT)
async def text_handler(message: types.Message):
    proverbs = get_proverbs(message.text)
    if not proverbs:
        await message.reply("Результаты не найдены :(")
        return

    keyboard = types.inline_keyboard.InlineKeyboardMarkup()

    if len(proverbs) > MAX_RESULTS_NUMBER:
        keyboard.insert(
            types.inline_keyboard.InlineKeyboardButton(text="➡", callback_data="10"))

    message_text = ''
    for num, proverb in enumerate(proverbs[:MAX_RESULTS_NUMBER]):
        message_text += f"{num + 1}. {proverb}\n"

    await message.reply(message_text, reply_markup=keyboard)
