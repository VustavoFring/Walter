# подключаем библиотеку
import 

import telebot
import random

# создаем токен для подключения к боту
token = '6383905722:AAGcegcN3WoHVi79GP6v_WtWbQ7o6V9_VFQ'

# создаем обьект для управления ботом
Jackob_bot = telebot.TeleBot(token)

# учим бота здороваться
# в скобках - обьект обработки
@Jackob_bot.message_handler(commands = ['start','help'])
def welcome_message(mess):
    # message - то,что пользаватель передал боту
    welcome_text = 'привет,я бот Jackob'
    Jackob_bot.send_message(mess.chat.id, welcome_text)

# учим бота отправлять котиков
@Jackob_bot.message_handler(commands = ['cat'])
def send_cat(mess):
    cat_num = random.randint(1,10)
    # открываем картинку
    cat_img = open('img/'+str(cat_num)+'.jpg','rb')

    Jackob_bot.send_photo(mess.chat.id, cat_img)


@Jackob_bot.message_handler(content_types=['text'])
# message - то, что написал пользователь боту
def send_answer(message):
    print(message)
    if 'привет' in message.text.lower():
        welcome_message(message)



Jackob_bot.polling()