import random
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

TOKEN = os.getenv("8528621931:AAHSVJNUG5DQbM21avM2qZNeR7xNH_IG32I")

bot = Bot(token=TOKEN)
dp = Dispatcher()

gifts = [
    "🎁 Ты получил золотую звезду!",
    "🎉 Тебе подарили торт!",
    "💎 Ты получил алмаз!",
    "🚗 Тебе подарили машину!",
    "🏆 Ты получил кубок!"
]

@dp.message(Command("start"))
async def start(message: Message):
    await message.answer("Привет! Напиши /gift 🎁")

@dp.message(Command("gift"))
async def gift(message: Message):
    await message.answer(random.choice(gifts))

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
