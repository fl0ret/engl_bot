# English Learning Bot

A bot for learning English in Telegram. Allows the user to practice words, test knowledge and receive daily tasks.

## Features
- Learning new words and phrases
- Testing knowledge through quizzes
- Generating exercises and repeating what has been learned
- Simple and convenient code structure

## Installation

1. Clone the repository:
git clone https://github.com/yourusername/english_bot.git
cd english_bot.

2. Create a virtual environment:
python -m venv venv
source venv/bin/activate  # for Linux/Mac
venv\Scripts\activate     # for Windows

3. Install dependencies:
pip install -r requirements.txt

4. Create a .env file with the bot and AI token:
AI_TOKEN=your_AI_token
TOKEN=your_bot_token

5.Launch the bot:
enter into the console: python main.py

## Project structure
main.py — entry point
config.py — token
generate.py — word/test generation
learn.py — main learning functionality
utils.py — auxiliary functions
requirements.txt — project dependencies

Technologies:
Python 3.10+
Telegram Bot API
AI API - You can connect them from different services, sites
aiogram - required library
