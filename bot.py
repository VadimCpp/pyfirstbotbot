import telebot
import logging
import os
from config import *
from flask import Flask, request

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')  # Ну это по классике, логи
logger = logging.getLogger()

MODE = Config.MODE
TOKEN = Config.BOT_TOKEN
URL = Config.URL

bot = telebot.TeleBot(Config.BOT_TOKEN)  # Создает объект класса "TeleBot", то есть нашего бота

def init_server():
	server = Flask(__name__)

	# Инициализирует webhook
	@server.route("/")
	def webhook():
		bot.remove_webhook()
		bot.set_webhook(url=URL + TOKEN)
		return "!", 200

	# Обработывает события
	@server.route('/' + TOKEN, methods=['POST'])
	def getMessage():
		bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
		return "!", 200

	return server

@bot.message_handler(
    content_types=['text', 'audio', 'document', 'photo', 'sticker', 'video', 'video_note', 'voice', 'location',
                   'contact', 'new_chat_members', 'left_chat_member', 'new_chat_title', 'new_chat_photo',
                   'delete_chat_photo', 'group_chat_created', 'supergroup_chat_created', 'channel_chat_created',
                   'migrate_to_chat_id', 'migrate_from_chat_id',
                   'pinned_message'])  # декоратор который заставляет пользователя реагировать на новые сообщения
def sending_auto2(message):
    bot.send_message(chat_id=message.chat.id, text=autosending_text(bot, message), parse_mode='html',
                     disable_web_page_preview=True)  # Отправляет авто сообщение

if __name__ == '__main__':
	logging.info("Selected mode " + MODE)
	if MODE == "debug":
		bot.remove_webhook()
		bot.polling() # Заставляет бота получать уведомления о новых сообщениях
	else:
		# Сервер необходим для работы webhook
		server = init_server()
		server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))

