import logging

from aiogram import types
from config import MAX_RESULTS_NUMBER
from dispatcher import dp

from .proverbs_functions import get_proverbs


@dp.callback_query_handler(lambda callback_query: True)
async def callback_handler(query: types.CallbackQuery):
    pointer = int(query.data)

    proverbs = get_proverbs(query.message.reply_to_message.text)
    if not proverbs:
        logging.error("No proverbs")
        return

    keyboard = types.inline_keyboard.InlineKeyboardMarkup()

    if pointer - MAX_RESULTS_NUMBER >= 0:
        prev_btn = types.inline_keyboard.InlineKeyboardButton(text="⬅", callback_data=str(pointer - MAX_RESULTS_NUMBER))
        keyboard.insert(prev_btn)

    if len(proverbs) > pointer + MAX_RESULTS_NUMBER:
        next_btn = types.inline_keyboard.InlineKeyboardButton(text="➡", callback_data=str(pointer + MAX_RESULTS_NUMBER))
        keyboard.insert(next_btn)

    message_text = ''
    for num, proverb in enumerate(proverbs[pointer: pointer + MAX_RESULTS_NUMBER]):
        message_text += f"{pointer + num + 1}. {proverb}\n"

    await query.message.edit_text(message_text, reply_markup=keyboard)
