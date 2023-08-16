# работа с tkinter

# импортировать tkinter
from tkinter import *

# функция для кнопки
def check_answer():
    # делаем так что бы переменные были доступны внутри фунции
    global current_q,points # - делаем переменные глобальными
    answer = variant.get()
    # проверка ответа
    if bool(answer) == facts[current_q]['right']:
        points += 1
        # проверка,остались ли вопросы
    if current_q < len(facts) - 1:
        current_q += 1  
        fact['text'] = facts[current_q]['text']
    else:
        points_lable = Label(text='ваши очки:'+ str(points),font=('Arial',24),fg='blue',bg='black')
        points_lable.place(x=0,y=0,width=700,height=500)


# создаем главное окно
window = Tk()
# задаем размеры окна
window.geometry('700x500')
# зациклить окно
# window.mainloop() # - последняя строчка

# создаем викторину с вопросами да\нет
# задаем название окну
window.title('Самая сложная викторина')
# список с фактами
facts = [
    {'text':'бабочки живут один день','right':0},
    {'text':'Спанч Боб это губка','right':1},
    {'text':'у марса два спутника','right':1},
    {'text':'Самый большой океан - это Тихий океан','right':1},
    {'text':'Лучший друг спанч боба - это сквидвард','right':0}
]
# номер вопроса
current_q = 0
# кол-во очков
points = 0
# создаем обьект однострочного текста
test_title = Label(text= 'самый сложный тест', font= ('Arial',24),fg='blue',bg= 'black')
# размещаем текст на окне
test_title.place(x=0,y=0,width=700,height=50)
# создаем обьект многострочного текста
fact = Message(text=facts[current_q]['text'],font=('Arial',14), width=680)
# размещаем факт на окне
fact.place(x=10,y=70)

# создаем кнопки для выбора ответа

# создаем целочисленный обьект
variant = IntVar()

true_button = Radiobutton(text='Правда', variable=variant, value= 1) 
false_button = Radiobutton(text='Ложь', variable=variant, value= 0)
true_button.place(x=10,y=120)
false_button.place(x=10,y=160)

# создаем кнопку ответить
answ = Button(text='ответить',font=('Arial',14),fg='black',command=check_answer)
answ.place(x=100,y=300)

window.mainloop()





