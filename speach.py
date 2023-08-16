# распознавание речи
import pygame
from gtts import gTTS
'''

# # создаем строку с текстом
# mytext = input('введите текст: ')

# открываем файл с текстом
file = open('data.txt',encoding='utf-8')
mytext= file.read()
file.close

# генерируем mp3 файл с текстом
file_mp3= gTTS(text=mytext,lang='ru')
# сохраняем файл в папку
file_mp3.save('sond.mp3')


# делаем воспроизведение файла с звуком
pygame.init()
# загружаем файл в программу
pygame.mixer.music.load('sond.mp3')
# воспроизводим файл
pygame.mixer.music.play(1)

# костыль для воспроизведения 
while True:
    pass
    '''

# ---------------------------------------------------------------------------------------------------


import speech_recognition as sr

# делаем обьект для распознования речи
rec = sr.Recognizer()
microfone = sr.Microphone(device_index=1)
# обьявляем бесконечный цикл
while True:
    with microfone as source:
        print('скажите что нибудь:')
        # получаем аудио сигнал от пользователя
        audio = rec.listen(source)
    # распознаем аудио и получаем строку
    speech =rec.recognize_google(audio,language='ru_RU').lower()
    print('вы сказали:',speech)
    if 'привет' in speech:
        print('привет пользователь!')