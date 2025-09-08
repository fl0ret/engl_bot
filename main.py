import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.enums import ParseMode
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN
from generate import ask_ai
from learn import (
    get_grammar_prompt,
    get_word_definition_prompt,
    get_translation_prompt,
    get_conversation_prompt,
)
from utils import clean_text

logging.basicConfig(level=logging.INFO)

from learn import generate_daily_words_via_ai

# Создание бота и диспетчера для aiogram 3.x
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

user_mode = {}


def create_main_keyboard():
    keyboard = ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="/translate"), KeyboardButton(text="/define")],
            [KeyboardButton(text="/grammar"), KeyboardButton(text="/chat")],
            [KeyboardButton(text="/words")]
        ],
        resize_keyboard=True,
        input_field_placeholder="Выберите режим"
    )
    return keyboard



@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "👋 Привет! Я бот для изучения английского языка.\n\n"
        "Команды:\n"
        "/translate — перевести текст\n"
        "/define — объяснение слова\n"
        "/grammar — объяснение грамматики\n"
        "/chat — диалог на английском\n"
        "/words - 5 рандомных слов",
        reply_markup=create_main_keyboard()
    )

@dp.message(Command("translate"), lambda message: message.text.startswith("/translate"))
async def cmd_translate(message: types.Message):
    user_mode[message.from_user.id] = "translate"
    await message.answer("📝 Отправь текст для перевода.")

@dp.message(Command("define"), lambda message: message.text.startswith("/define"))
async def cmd_define(message: types.Message):
    user_mode[message.from_user.id] = "define"
    await message.answer("🔍 Введи слово на английском.")

@dp.message(Command("grammar"), lambda message: message.text.startswith("/grammar"))
async def cmd_grammar(message: types.Message):
    user_mode[message.from_user.id] = "grammar"
    await message.answer("📚 Введи грамматическую тему.")

@dp.message(Command("chat"), lambda message: message.text.startswith("/chat"))
async def cmd_chat(message: types.Message):
    user_mode[message.from_user.id] = "chat"
    await message.answer("💬 Напиши что-нибудь — поболтаем на английском!")

@dp.message(Command("words"), lambda message: message.text.startswith("/words"))
async def send_daily_words(message: types.Message):
    await message.answer("Генерирую слова дня, подождите...")
    result = generate_daily_words_via_ai()
    await message.answer(result)


@dp.message()
async def handle_user_input(message: types.Message):
    user_id = message.from_user.id
    mode = user_mode.get(user_id)

    if not mode:
        return  

    text = clean_text(message.text)

    try:
        if mode == "translate":
            prompt = get_translation_prompt(text)
            system = "Ты профессиональный переводчик. Переводи между английским и русским. Только перевод."
        elif mode == "define":
            prompt = get_word_definition_prompt(text)
            system = "Ты словарь английского. Объясни слово простыми словами с примером."
        elif mode == "grammar":
            prompt = get_grammar_prompt(text)
            system = "Ты преподаватель английского. Объясни грамматику понятно и с примерами."
        elif mode == "chat":
            prompt = text
            system = get_conversation_prompt()

        response = await ask_ai(prompt, system)
        await message.answer(response)

    except Exception:
        logging.exception("AI error")
        await message.answer("⚠️ Произошла ошибка при обращении к ИИ.")


if __name__ == "__main__":
    # Запуск бота
    asyncio.run(dp.start_polling(bot))


