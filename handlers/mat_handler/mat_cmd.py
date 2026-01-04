from aiogram import Router, Bot

from aiogram.filters import Command

from aiogram.types import Message

from handlers.mat_handler.class_mat import ObrabotkaMat

from handlers.text_from_user import text_rus

router = Router()


@router.message(Command(commands='mat'))
async def off_true_mat(message: Message, bot: Bot):
    '''Функция для разрешения обработки команды по замене мата'''
    get_chat = await bot.get_chat_administrators(chat_id=message.chat.id)
    user_admin: list = [user_info.user.id for user_info in get_chat]

    if message.from_user.id in user_admin:
        if ObrabotkaMat.chat.get(message.chat.id) is None:
            ObrabotkaMat.set_chat(message.chat.id, True)
            await message.answer(text=text_rus['mat']['true'])

        elif ObrabotkaMat.chat[message.chat.id] == True:
            ObrabotkaMat.set_chat(message.chat.id, False)
            await message.answer(text=text_rus['mat']['false'])
            
        elif ObrabotkaMat.chat[message.chat.id] == False:
            ObrabotkaMat.set_chat(message.chat.id, True)
            await message.answer(text=text_rus['mat']['true'])
    else:
        await message.answer(text=text_rus['mat']['none'])
    await message.delete()
