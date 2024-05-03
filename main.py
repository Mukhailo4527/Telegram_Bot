from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton
from config import *

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)
kb = ReplyKeyboardMarkup(resize_keyboard=True)
b1="/start"
b2="/help"
b3="/buy_pizza"
b4="/big"
b5="/small"
b6="/peperoni"
b7="/margarita"
b8="/mushroom"
b9="/done"
b10="/cansel"
kb.add(b1).add(b2).add(b3).add(b4).insert(b5).add(b6).insert(b7).insert(b8).add(b9).insert(b10)


@dp.message_handler(commands=['start'])
async def helper(message: types.Message):
        await bot.send_message(chat_id=message.from_user.id,
                               text=start_text,
                               reply_markup=kb)

@dp.message_handler(commands=['help'])
async def helper(message: types.Message):
        await message.reply(text=help_text)

@dp.message_handler(commands=['buy_pizza'])
async def helper(message: types.Message):
        await message.reply(text=buy_pizza1)

@dp.message_handler(commands=['big'])
async def helper(message: types.Message):
        global size
        size = 2
        await message.reply(text=buy_pizza2)


@dp.message_handler(commands=['small'])
async def helper(message: types.Message):
        await message.reply(text=buy_pizza2)
        global size
        size = 1



@dp.message_handler(commands=['peperoni'])
async def helper(message: types.Message):
        globals()
        price = peperoni * size
        await message.reply(text=f'ця піца коштуватиме {price}, щоб підтвердити покупку використайте /done, щоб відманити покупку введіть /cansel')


@dp.message_handler(commands=['margarita'])
async def helper(message: types.Message):
        globals()
        price = margarita * size
        await message.reply(text=f'ця піца коштуватиме {price}, щоб підтвердити покупку використайте /done, щоб відманити покупку введіть /cansel')

@dp.message_handler(commands=['mushroom'])
async def helper(message: types.Message):
        globals()
        price = mushroom * size
        await message.reply(text=f'ця піца коштуватиме {price}, щоб підтвердити покупку використайте /done, щоб відманити покупку введіть /cansel')

@dp.message_handler(commands=['cansel'])
async def helper(message: types.Message):
        global size
        global price
        price = 0
        size = 0
        await message.reply(text='ви успішно відмінили покупку, щоб почати нове замовлення введіть /buy_a_piza')


@dp.message_handler(commands=['done'])
async def helper(message: types.Message):
        c = 'тут ви зможете забрати свою піцу'
        await message.reply(text=c)
        await bot.send_location(chat_id=message.from_user.id,
                                latitude=49.959702, longitude=36.324846)
        await message.reply(text=end)


if __name__ == '__main__':
    executor.start_polling(dp,skip_updates=True)