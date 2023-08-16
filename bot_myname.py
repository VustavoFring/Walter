import telebot
token = '6383685585:AAE8b6uSUlukPUfNfs1oGlcLQXu_nxmZg2E'
botMyName = telebot.TeleBot(token)
@botMyName.message_handler(commands=['start'])
def start(message):
    botMyName.send_message(message.chat.id,'Привет! Меня зовут бот, я умею знакомиться, напиши слово - привет')


@botMyName.message_handler(content_types=['text'])
def get_messages(message):
    if message.text.lower() == 'привет':
        botMyName.send_message(message.from_user.id, 'Привет, напиши свое имя и мы сможем познакомиться!') 
        botMyName.register_next_step_handler(message, get_surname)


def get_surname(message):
    global name
    name = message.text
    botMyName.send_message(message.from_user.id, 'A какая y тебя фамилия?')
    botMyName.register_next_step_handler(message, get_result)
    
                           
def get_result(message):
    global surname
    surname = message.text
    botMyName.send_message(message.from_user.id,'Тебя зовут ' + name + ' ' + surname + '. Очень приятно познакомиться!')


botMyName.polling(none_stop=True, interval=0)