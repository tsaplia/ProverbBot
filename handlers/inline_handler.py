from aiogram import types
from config import MAX_RESULTS_NUMBER, CACHE_TIME
from dispatcher import dp

from .proverbs_functions import get_proverbs


@dp.inline_handler()
async def inline_handler(query: types.InlineQuery):
    proverbs = get_proverbs(query.query)
    if not proverbs:
        result = types.InlineQueryResultArticle(
            id='1',
            title="Результаты не найдены :(",
            input_message_content=types.InputTextMessageContent(
                parse_mode='HTML',
                message_text=f"{query.query} <b></b>Результаты не найдены")
        )
        await query.answer(results=[result], cache_time=CACHE_TIME)
        return

    offset = int(query.offset) if query.offset else 0
    next_offset = str(MAX_RESULTS_NUMBER + offset) if len(proverbs) > MAX_RESULTS_NUMBER + offset else ''
    results = []

    for num, proverb in enumerate(proverbs[offset:MAX_RESULTS_NUMBER + offset]):
        results.append(types.InlineQueryResultArticle(
            id=str(num + offset),
            title=proverb,
            description=proverb,
            input_message_content=types.InputTextMessageContent(
                message_text=proverb))
        )

    await query.answer(results=results, cache_time=CACHE_TIME, next_offset=next_offset)
