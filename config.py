import os
import dotenv # Необходима для использования переменных среды  из .env файла

from telebot.types import InlineKeyboardButton

dotenv.load_dotenv()

class Config:
    MODE = os.getenv('MODE')
    BOT_TOKEN = os.getenv('BOT_TOKEN')
    URL = os.getenv('HEROKU_URL')


def autosending_text(bot, message):
    first_name = bot.get_chat(message.chat.id).first_name
    text = """Hello, {0}
This is the starter template for other bots built with <b>python</b>. 
No bots cooked so far.
Enjoy cooking with <a href = 'https://github.com/VadimCpp/pyfirstbotbot'>this template</a>!""".format(first_name)
    return text
