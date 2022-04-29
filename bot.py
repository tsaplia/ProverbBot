import logging
from aiogram import executor

from dispatcher import dp
import handlers


if __name__ == "__main__":
    try:
        executor.start_polling(dp, skip_updates=True)
    except Exception as e:
        logging.error('Exception occurred',exc_info=True)

