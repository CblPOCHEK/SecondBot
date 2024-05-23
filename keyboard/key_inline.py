from aiogram. types import InlineKeyboardMarkup, InlineKeyboardButton

def get_keyboard_inline():
    keyboard_inline = InlineKeyboardMarkup(row_width=1)
    but_inline = InlineKeyboardButton(text='Посмотреть', url='https://www.purina.ru/cats/breed-Library')
    but_inline2 = InlineKeyboardButton(text='Посмотреть', url='https://www.purina.ru/cats/breed-library')
    keyboard_inline.add(but_inline, but_inline2)
    return keyboard_inline
