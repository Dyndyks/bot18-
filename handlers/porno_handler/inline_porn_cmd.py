from aiogram import Router, Bot

from aiogram.filters import Text

from aiogram.types import CallbackQuery, InputMediaPhoto

from create_keyboard.my_keyboard import create_inline_kb

from handlers.porno_handler.func_porno import get_set_video, get_video, UserGetVideo

from asyncio import sleep as ao_sleep


router = Router()


@router.callback_query(Text(text=['lesbiyanki', 'masturbation', 'classic']))
async def get_porno(callback: CallbackQuery, bot: Bot):
    '''Функция для обработки выбранной категории видео'''
    in_kb = create_inline_kb(
        2,
        left='<',
        right='>',
        exit_menu='назад'

    )
    UserGetVideo.get_content_count(
        callback.data,
        get_video(callback.data)
    )

    count = UserGetVideo.d[callback.data]['count']
    content = UserGetVideo.d[callback.data]['content']
    photo = content[count][0]
    text = content[count][1]
    url = content[count][2]
    user = callback.message.chat.id

    await callback.message.delete()
    await bot.send_photo(
            chat_id=user,
            photo=photo,
            caption=f"<a href='{url}'>{text}</a>",
            parse_mode='HTML',
            reply_markup=in_kb.as_markup()
            )
    

@router.callback_query(Text(text=['left', 'right']))
async def scroll_through_porno(callback: CallbackQuery, bot: Bot):
    '''Функция для пролистывание видео'''
    content = get_set_video('-') if callback.data == 'left' else get_set_video('+')
    await callback.answer('обновляю')
    await ao_sleep(1)
    await bot.edit_message_media(
        media=InputMediaPhoto(
            type='photo',
            media=content[0],
            caption=f"<a href='{content[2]}'>{content[1]}</a>",
            parse_mode='HTML'
        ),
        chat_id=callback.message.chat.id,
        message_id=callback.message.message_id,
        reply_markup=callback.message.reply_markup
    )


@router.callback_query(Text(text='exit_menu'))
async def get_menu_porn(callback: CallbackQuery):
    '''Функция для возвращения к выбору категорий'''
    for date in UserGetVideo.lst:
        if UserGetVideo.d.get(date):
            del UserGetVideo.d[date]

    in_kb = create_inline_kb(
        3,
        lesbiyanki='лесбиянки',
        masturbation='мастурбация',
        classic='классика',
        exit_='выход'
        )
    
    await callback.message.delete()
    await callback.message.answer(
        text='выбери категорию:',
        reply_markup=in_kb.as_markup()
    )


@router.callback_query(Text(text='exit_'))
async def exit_porno(callback: CallbackQuery):
    '''Функция для прекращения работы команды'''
    await callback.message.delete()