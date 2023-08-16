# Парсинг API Центробанка
import requests
from tkinter import *
from bs4 import BeautifulSoup
# библиотека для даты
from datetime import datetime

# создаем функцию для получения данных
def get_data(id):
    return xml.find('Valute',{'ID': id}).Value.text

# создаем главное окно
window = Tk()
window.geometry('400x350')
window.title('курс валют')



url = 'http://www.cbr.ru/scripts/XML_daily.asp?date_req='
# получаем сегодняшнюю дату
today = datetime.today()
# конвертируем дату в правильный формат дд/мм/гггг
today = today.strftime('%d/%m/%Y')
# делаем запрос к api 
request = requests.get(url+today)

# формируем xml файл
xml = BeautifulSoup(request.content, features='xml')

# получаем данные о долларе и евро
# print(get_data('R01235'),'рублей за 1 доллар')
# print(get_data('R01239'),'рублей за 1 евро')


# добовляем лого
logo = PhotoImage(file='logo.png')
Label_logo = Label(window,image= logo)
Label_logo.place(x= 0,y= 0)

# создаем название программы
name_prog = Label(window,text='Курс валют \n Central Bank',fg='black',font='Arial 22')
name_prog.place(x=150,y=25)

# размещаем сегодняшнюю дату на окне
date = Label(window,text='Курс валют на '+ today,fg='black',font='Arial 16')
date.place(x=90,y=150)

# размещаем курс доллара
usd = Label(window, text='$ '+get_data('R01235'), font='Arial 16')
usd.place(x=90,y=190)

# размещаем курс евро
eur = Label(window, text='€ '+get_data('R01239'), font='Arial 16')
eur.place(x=90,y=230)

window.mainloop()