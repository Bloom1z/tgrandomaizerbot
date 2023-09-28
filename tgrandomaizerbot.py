# Импортирование библиотек
from aiogram import Bot, Dispatcher, executor, types
from app import keyboards as kb
import random
from dotenv import load_dotenv
import os


# Инициализация бота
load_dotenv()
bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot=bot)


# Обработчик команды /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.answer('''Привет я Бот Рандомайзер.
Выберите способ генерации:''', reply_markup=kb.keyboard_random)


# Да или Нет
yes_or_no = ['✅Да', '❌Нет']


# Обработчик игры Да или Нет
@dp.message_handler(lambda message: message.text == '✅Да или ❌Нет')
async def cmd_yes_or_no(message: types.Message):
    await message.answer(f'{random.choice(yes_or_no)}')


# Камень, Ножницы, Бумага
rock_scissors_paper = ['👊Камень', '✌️Ножницы', '🖐️Бумага']


# Обработчик игры Камень, Ножницы, Бумага
@dp.message_handler(lambda message: message.text == '👊Камень,✌️Ножницы,🖐️Бумага')
async def cmd_rock_scissors_paper(message: types.Message):
    await message.answer(f'{random.choice(rock_scissors_paper)}')


# Обработчик игры случайное число от 0 до 10
@dp.message_handler(lambda message: message.text == '🎲Случайное число от 0 до 10')
async def cmd_random_number_from1to10(message: types.Message):
    await message.answer(f'{random.randint(0,10)}')


# Список для игры Слово или Слово
words_list_word_or_word = []


# Обработчик игры слово или слово
@dp.message_handler(lambda message: message.text == '🔤Слово или слово')
async def cmd_word_or_word(message: types.Message):
    await message.answer(f'📝1/2 Введите первое слово:')

    @dp.message_handler(lambda message: len(words_list_word_or_word) == 0)
    async def handle_first_word(message: types.Message):
        word = message.text
        words_list_word_or_word.append(word)
        await message.answer('📝2/2 Отлично! Теперь введите второе слово:')

        @dp.message_handler(lambda message: len(words_list_word_or_word) == 1)
        async def handle_second_word(message: types.Message):
            word = message.text
            words_list_word_or_word.append(word)
            await message.answer(f'Случайно выбранное слово : {random.choice(words_list_word_or_word)}', reply_markup=kb.keyboard_word_or_word_again)

            @dp.callback_query_handler(text='word_or_word_again')
            async def cmd_random_word_again(call_again: types.CallbackQuery):
                await call_again.message.answer(f'Случайно выбранное слово : {random.choice(words_list_word_or_word)}', reply_markup=kb.keyboard_word_or_word_again)
    words_list_word_or_word.clear()

    @dp.callback_query_handler(text='word_or_word_back')
    async def cmd_word_back(call_back: types.CallbackQuery):
        await call_back.message.answer(f'Выберите способ генерации:', reply_markup=kb.keyboard_random)


# Список для игры Подбросить монетку
list_toss_coin = ['🦅Орел', '🪙Решка']


# Обработчик игры Подбросить монетку
@dp.message_handler(lambda message: message.text == '🪙Подбросить монетку')
async def cmd_toss_coin(message:types.Message):
    await message.answer(f'{random.choice(list_toss_coin)}')


# Список для игры Случайное число от и до
list_random_number_from_to = []


# Обработчик игры Случайное число от и до
@dp.message_handler(lambda message: message.text == '🎲Случайное число от и до')
async def cmd_random_number_from_to(message: types.Message):
    await message.answer(f'📝1/2 Введите от скольки генерировать число:')

    @dp.message_handler(lambda message_first_num: len(list_random_number_from_to) == 0)
    async def handle_first_number(message: types.Message):
        if message.text.isdigit() is False:
            await message.answer(f'Введите ЧИСЛО!', reply_markup=kb.keyboard_random_number_else)
        else:
            number_first = int(message.text)
            list_random_number_from_to.append(number_first)
            await message.answer(f'📝2/2 Хорошо! Теперь введите второе число:')

            @dp.message_handler(lambda message_second_num: len(list_random_number_from_to) == 1)
            async def handle_second_number(message: types.Message):
                if message.text.isdigit() is False:
                    await message.answer(f'Введите ЧИСЛО!', reply_markup=kb.keyboard_random_number_else)
                else:
                    number_second = int(message.text)
                    list_random_number_from_to.append(number_second)
                    await message.answer(f'Случайно выбранное число : {random.randint(list_random_number_from_to[0], list_random_number_from_to[1])}', reply_markup=kb.keyboard_random_num_again)

            @dp.callback_query_handler(text='random_number_again')
            async def cmd_random_number_again(call_again: types.CallbackQuery):
                await call_again.message.answer(f'Случайно выбранное число : {random.randint(list_random_number_from_to[0], list_random_number_from_to[1])}', reply_markup=kb.keyboard_random_num_again)
    list_random_number_from_to.clear()

    @dp.callback_query_handler(text='random_number_back')
    async def cmd_word_back(call_back: types.CallbackQuery):
        await call_back.message.answer(f'Выберите способ генерации:', reply_markup=kb.keyboard_random)


# Список для игры Случайное слово
list_random_word = []


# Обработчик игры Случайное слово
@dp.message_handler(lambda message: message.text == '🔤Случайное слово')
async def cmd_random_word(message: types.Message):
    await message.answer(f'📝Введите несколько слов через запятую:')

    @dp.message_handler(lambda message: len(list_random_word) == 0)
    async def handle_words(message: types.Message):
        list_random_word.extend(message.text.split(','))
        await message.answer(f'Случайно выбранное слово : {random.choice(list_random_word)}', reply_markup=kb.keyboard_random_word_again)

        @dp.callback_query_handler(text='random_word_again')
        async def cmd_random_word_again(call: types.CallbackQuery):
            await call.message.answer(f'Случайно выбранное слово : {random.choice(list_random_word)}', reply_markup=kb.keyboard_random_word_again)
    list_random_word.clear()

    @dp.callback_query_handler(text='random_word_back')
    async def cmd_random_word_back(call: types.CallbackQuery):
        await call.message.answer(f'Выберите способ генерации:', reply_markup=kb.keyboard_random)


# Запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)