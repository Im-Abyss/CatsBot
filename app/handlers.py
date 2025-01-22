import asyncio
import aiohttp
from aiogram import Router, F
from aiogram.filters import CommandStart
from aiogram.types import Message

import app.keyboards as kb

router = Router()

# Приветственное сообщение с Reply-клавиатурой
@router.message(CommandStart())
async def welcome(message: Message):
    await message.answer('Привет! Нажми кнопку ниже, чтобы получить фотку котика и поднять себе настроение! 🐱', reply_markup=kb.add_cats)


@router.message(F.text == "Фото котиков 🐱")
async def send_cat_photo(message: Message):
    async with aiohttp.ClientSession() as session:

        while True:
            async with session.get('https://api.thecatapi.com/v1/images/search') as response:  # Отправляем GET-запрос к API сайта

                if response.status == 200:  # Проверяем, успешен ли запрос
                    data = await response.json()
                    if data:  # Проверяем, есть ли данные в ответе         
                        photo_url = data[0]['url']
                        await message.answer_photo(photo_url)
                        break  # Если фото успешно отправлено, выходим из цикла
                    else:
                        print("Фото не найдено, пробуем снова...")  # Если данные пустые, выводим сообщение и продолжаем цикл

                # Обработка ошибок
                if response.status == 522:
                    print("Ошибка 522: Проблема с соединением. Повторяем запрос...")
                else:
                    print(f"Ошибка запроса к The Cat API: {response.status}. Попробуем снова...")

            # Задержка перед повторным запросом, чтобы избежать перегрузки сервера
            await asyncio.sleep(1)