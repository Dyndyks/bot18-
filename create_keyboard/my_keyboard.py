from aiogram.types import InlineKeyboardButton, KeyboardButton

from aiogram.utils.keyboard import InlineKeyboardBuilder, ReplyKeyboardBuilder

def create_inline_kb(size: int, **kwargs) -> InlineKeyboardBuilder:
    ink: InlineKeyboardBuilder = InlineKeyboardBuilder()
    for button, text in kwargs.items():
        ink.add(InlineKeyboardButton(text=text, callback_data=button))
    ink.adjust(size)
    return ink

def create_kb(size: int, *args) -> ReplyKeyboardBuilder:
    ink: ReplyKeyboardBuilder = ReplyKeyboardBuilder()
    for text in args:
        ink.add(KeyboardButton(text=text))
    ink.adjust(size)
    return ink