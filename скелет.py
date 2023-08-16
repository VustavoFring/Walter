# 'компьютерный вирус'
from tkinter import *


# функция обратного отсчета
def count_start():
    # проверка что счетчик не достиг нуля
    if int(danger_counter['text']) > 0:
        danger_counter['text'] = int(danger_counter['text']) -1
        danger_counter.place(x=250,y=25,width=400,height=100)
        # делаем обратный отсчет через 1 секунду
        window.after(1000, count_start)
    # проверка что счетчик достиг нуля 
    else:
        # делаем что бы окно открылось на весь экран
        # получаем ширину экрана 
        width = window.winfo_screenwidth()
        height = window.winfo_screenheight()
        # меняем размер
        window.geometry(str(width)+'x'+ str(height))
        skelet = PhotoImage(file='skelet.gif')
        skelet_label = Label(image=skelet,bg='black')
        skelet_label.image = skelet
        skelet_label.place(x=0,y=0,width=width,height=height)


# задаем функцию отрабатывающую закрытие окна
def one_close():
    # вызываем функцию обратного отсчета
    count_start()

# главное окно
window = Tk()
window.geometry('900x300')
window.title('опасность!!!')
# задний фон окна темный
window.config(bg = 'black')
# окно не может изменит размер
window.resizable(width=False , height=False)
danger_text = Label(text='ваш компьютер заражен',fg='green',bg='black',font=('Courier New',34))
danger_text.place(x=100,y=100,width=700,height=100)

# создаем сечетчик для пользователя
danger_counter = Label(text='11',fg='green',bg='black',font=('Courier New',34))


# окно нельзя закрыть на крестик
# one_close - функция которая сработает после указанного события
window.protocol('WM_DELETE_WINDOW', one_close )




window.mainloop()