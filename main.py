from aiogram import Dispatcher, Bot, types
from aiogram.utils import executor
from Token import Token
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, ReplyKeyboardRemove

bot = Bot(Token)
dp = Dispatcher(bot)

async def on_startup(_):
    print("Бот запущен")

Help_command = """
/help - список команд
/как получить бонусные баллы
количество бонусных балов
/start - начать роботу с ботом
/give or /sticker - отправит забавное емодзи

"""
bal = "Баллы можно получить за:" \
      "Подписку = 10," \
      "Отправку посылки = 5" \
      "За хороший коментарий = 1"

count = 0

kb = ReplyKeyboardMarkup(resize_keyboard=True)
kb.add(KeyboardButton('/help'))
@dp.message_handler(commands=["help"])
async def first(message: types.Message):
    await message.answer(text=Help_command, parse_mode="HTML")

@dp.message_handler(commands=["как получить бонусные баллы"])
async def how_ball(message: types.Message):
    await message.answer(text=bal, parse_mode="HTML")

@dp.message_handler(commands=["количество бонусных балов"])
async def amount(message: types.Message):
    await message.answer(text=f"{count} баллов", parse_mode="HTML")

@dp.message_handler(commands=['sticker'])
async def send_s(message: types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAMlY1uT6l3BQbAyIOG2SPufQs0WlxwAAgoYAAJhnqlKYhPAzdfzNKQqBA")

@dp.message_handler(commands=['start'])
async def starts(message= types.Message):
    await message.answer(text=f"<em>Hello, {message.from_user.first_name}</em>", parse_mode="HTML", reply_markup=kb)
    # await message.answer()

@dp.message_handler(commands=['give'])
async def no_command(message=types.Message):
    await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEGOxZjW40KFOstRyvvBM7wOHgNv-uy3gACoxwAAsvSoEoKhTrlkmX3XCoE")



if __name__ == "__main__":
    executor.start_polling(dp, on_startup=on_startup)