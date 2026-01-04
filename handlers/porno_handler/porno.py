from aiogram import Router

from aiogram.filters import Command

from aiogram.types import Message

from create_keyboard.my_keyboard import create_inline_kb

from handlers.porno_handler.func_porno import proverka_date, get_url

from asyncio import sleep as ao_sleep


router = Router()


@router.message(Command(commands='porn'))
async def cmd_porn(message: Message):
    '''Функция для проверки даты и выбора категории'''
    date = proverka_date()

    if date:
        mes = await message.answer('сегодня день обновлений, прошу подождите немного')
        for url in ('', 'lesbiyanki', 'masturbation'):
            await ao_sleep(3)
            get_url(url)
        await mes.delete()
    
    in_kb = create_inline_kb(
        3,
        lesbiyanki='лесбиянки',
        masturbation='мастурбация',
        classic='классика',
        exit_='выход'
        )
    
    await message.answer(
        text='выбери категорию:',
        reply_markup=in_kb.as_markup()
    )