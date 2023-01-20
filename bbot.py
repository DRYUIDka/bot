import telebot
import random
import requests
from bs4 import BeautifulSoup as b 
from telegram import ReplyKeyboardMarkup, ReplyKeyboardRemove
from telegram.ext import Updater, MessageHandler, Filters, CommandHandler

APIshka = '5859227563:AAFY6BN6H9Acpw1i86C1gMqXrKaclCYeJNo'

URL = ('https://ru.stackoverflow.com/questions/tagged/python?sort=Newest&edited=true') #новые вопросы с сайта
def sort(URL):
    r = requests.get(URL, verify=False)
    soup = b(r.text, 'html.parser')
    quest = soup.find_all('div', class_=text)
    return [c.text for c in quest]
URL2 = ('https://ru.stackoverflow.com/questions/tagged/python?sort=MostVotes&edited=true') #популярные вопросы
def sortirovka(URL2):
    k = requests.get(URL2, verify=False)
    soup = b(r.text, 'html.parser')
    quest_p = soup.find_all('div', class_=text)
    return [l.text for l in quest_p]
list = parser(URL, URL2)
random.shuffle(list)

bot = telebot.Telebot(APIshka)
@bot.message_handler(commands=['start'])

def start(mess):
    bot.send_message(message.chat.id, 'Привет, чтобы начать нажми любую цифру')

@bot.message_handler(content_types=['text'])
def h(message):
    if message.text.lower() in '1234567890':
       bot.ssenf_message(message.chat.id, list[0])
       del list[0] 
    else:
        bot.ssenf_message(message.chat.id, 'Привет, чтобы начать нажми любую цифру')

bot.polling()

def popular(bot, update):
    update.message.reply_text(quest_p)
def new(bot, update):
    update.message.reply_text(quest)
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

dp.add_handler(CommandHandler('popular', popular))
dp.add_handler(CommandHandler('new', new))

text_handler = MessageHandler(Filters.text, start)
dp.add_handler(text_handler)

updater.start_polling()
updater.idle()
