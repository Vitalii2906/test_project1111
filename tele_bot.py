import asyncio
import logging
from aiogram import Bot, Dispatcher, types, F
from aiogram.filters.command import Command
from aiogram.enums.dice_emoji import DiceEmoji


# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
# Объект бота
bot = Bot(token="6169598571:AAFWyHbWoRzVu5eoMcWpcNk3IFQjx_y5DDM")
# Диспетчер
dp = Dispatcher()

@dp.message(Command("start"))
async def my_start(message: types.Message):
    await message.answer("Hello")

@dp.message(Command("button"))
async def cmd_start(message: types.Message):
    kb = [
        [types.KeyboardButton(text="Кнопка 1"), types.KeyboardButton(text="Кнопка 3")],
        [types.KeyboardButton(text="Кнопка 2")]
    ]
    keyboard = types.ReplyKeyboardMarkup(keyboard=kb)
    await message.answer("Вибери кнопку", reply_markup=keyboard)

@dp.message(Command("dice"))
async def cmd_dice(message: types.Message, bot: Bot):
    await bot.send_dice(message.chat.id, emoji=DiceEmoji.BASKETBALL)

@dp.message(F.text)
async def echo_message(message: types.Message):
    if message.text == "Кнопка 1":
        import requests
        response = requests.get("https://catfact.ninja/fact")

        await message.answer(response.content.decode("utf8"))
    await message.answer(message.text)

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())