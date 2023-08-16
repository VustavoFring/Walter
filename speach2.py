import speech_recognition as sr
import pygame
from gtts import gTTS
rec = sr.Recognizer()
microfone = sr.Microphone(device_index=1)
def recognize_speech():
    with microfone as source:
        print('скажи что-нибудь:')
        audio = rec.listen(source)
    try:
        text =rec.recognize_google(audio,language='ru_RU').lower()
        print(text)
    except sr.UnknownValueError:
        print('ваша реплика не распознана')
    except sr.RequestError as e:
        print('произошла ошибка запроса!')
while True:
    recognize_speech()
    
    

    


