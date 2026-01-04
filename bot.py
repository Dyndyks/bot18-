import asyncio

from aiogram import Bot, Dispatcher

from handlers import glav_cmd

from handlers.porno_handler import porno, inline_porn_cmd

from handlers.mat_handler import mat, mat_cmd



token = 'твой api'


async def main():
    bot: Bot = Bot(token)
    dp: Dispatcher = Dispatcher()

    dp.include_router(glav_cmd.router)
    dp.include_router(porno.router)
    dp.include_router(inline_porn_cmd.router)
    dp.include_router(mat_cmd.router)
    dp.include_router(mat.router)

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())