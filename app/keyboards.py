from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton


# Клавиатура рандомайзера
keyboard_random = ReplyKeyboardMarkup(resize_keyboard=True)
keyboard_random_buttons = [KeyboardButton(text='✅Да или ❌Нет'),
                            KeyboardButton(text='👊Камень,✌️Ножницы,🖐️Бумага'),
                            KeyboardButton(text='🔤Слово или слово'),
                            KeyboardButton(text='🪙Подбросить монетку'),
                            KeyboardButton(text='🎲Случайное число от и до'),
                            KeyboardButton(text='🔤Случайное слово'),
                            KeyboardButton(text='🎲Случайное число от 0 до 10'),
                            ]
column1 = keyboard_random_buttons[:3]
column2 = keyboard_random_buttons[3:]
keyboard_random.add(*column1).add(*column2)


# Клавиатура игры слово или слово
keyboard_word_or_word_again = InlineKeyboardMarkup(row_width=2)
keyboard_word_or_word_again.add(InlineKeyboardButton(text='🔁Повторить', callback_data='word_or_word_again'),
                                InlineKeyboardButton(text='⏪Назад', callback_data='word_or_word_back'))

keyboard_random_num_again = InlineKeyboardMarkup(row_width=2)
keyboard_random_num_again.add(InlineKeyboardButton(text='🔁Повторить',callback_data='random_number_again'),
                              InlineKeyboardButton(text='⏪Назад', callback_data='random_number_back'))

keyboard_random_word_again = InlineKeyboardMarkup(row_width=2)
keyboard_random_word_again.add(InlineKeyboardButton(text='🔁Повторить',callback_data='random_word_again'),
                              InlineKeyboardButton(text='⏪Назад', callback_data='random_word_back'))

keyboard_random_number_else = InlineKeyboardMarkup(row_width=1)
keyboard_random_number_else.add(InlineKeyboardButton(text='⏪Назад', callback_data='random_number_back'))
