
import random
import time
import telebot
from config import token
from botlogic import gen_pass
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Я твой Telegram бот. Напиши что-нибудь!")

@bot.message_handler(commands=['gen_password'])
def send_password(message):
    bot.send_message(message.chat.id, gen_pass(10))
bot.polling()