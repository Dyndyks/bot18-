from aiogram import Router

from aiogram.filters import Command

from aiogram.types import Message

from all_db.reg_user_class import DbRegUsers

from handlers.text_from_user import text_rus


router: Router = Router()


@router.message(Command(commands='start'))
async def cmd_start(message: Message):
    reg = DbRegUsers()
    reg.reg_user(message.from_user.id, message.from_user.full_name)
    await message.delete()
    await message.answer(
            text=text_rus['start']
        )


@router.message(Command(commands='help'))
async def cmd_help(message: Message):
    await message.delete()
    await message.answer(text=text_rus['help'], parse_mode='HTML')


@router.message(Command(commands='description'))
async def cmd_description(message: Message):
    await message.delete()
    await message.answer(text=text_rus['description'])