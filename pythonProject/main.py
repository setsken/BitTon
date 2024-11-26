import telebot
import os

# Получаем токен из переменной окружения
TOKEN = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Добро пожаловать в майнинг-бот. Используй /mine для добычи блоков!")

@bot.message_handler(commands=['mine'])
def mine(message):
    bot.reply_to(message, "Ты нашёл блок и получил награду!")

@bot.message_handler(commands=['balance'])
def balance(message):
    bot.reply_to(message, "Ваш баланс: 100 монет.")

bot.polling()
