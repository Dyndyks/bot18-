from aiogram import Router, F

from aiogram.types import Message

from aiogram.filters import Text

from handlers.mat_handler.class_mat import ObrabotkaMat

router = Router()


@router.message(
    lambda message: message.content_type == 'text' and
        ObrabotkaMat.proverka(message.text) and
        ObrabotkaMat.chat.get(message.chat.id) == True
)
async def msg_mat(message: Message):
    '''Функция для скрытия мата'''
    text = ObrabotkaMat.red_text(message.text)
    username = message.from_user.username
    await message.delete()
    await message.answer(
        text=f'{text}\n\nСообщение от @{username}',
        parse_mode='HTML'
    )