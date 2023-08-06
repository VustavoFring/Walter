# метод __add__

class item:
# комплектующие компьютера
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight
    # создаем метод __add__
    def __add__(self, other):
        if isinstance(other,item):
            return self.price + other.price
        elif isinstance(other,int) or isinstance(other,float):
            return self.price + other

itrm_gp = item('видеокарта', 50_000, 2)
item_cp = item('процессор', 20_000, 0.2)

# получаем суммарную стоимость 
total_price = item_cp + itrm_gp

# print(total_price)

# -------------------------------------------------------------------------------

# игра Алхимия
from tkinter import*
from random import randint

window = Tk()
window.geometry('600x600')

# создаем класс для огня
class Fire:
    image = PhotoImage(file='fire.png').subsample(4,4)
    # логика получения глины(огонь + земля)
    def __add__(self,other):
        if isinstance(other,Earth):
            return Clay

class Earth:
    image = PhotoImage(file='earth.png').subsample(4,4)
    # логика получения глины(огонь + земля)
    def __add__(self,other):
        if isinstance(other,Fire):
            return Clay
        
class Clay:
    image = PhotoImage(file='clay.png').subsample(4,4)

class Water:
    image = PhotoImage(file='water.png').subsample(4,4)

class Wind:
    image = PhotoImage(file='wind.png').subsample(4,4)

# функция перемещения элементов
def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x +5, event.y +5)
    # перемещаем изображение за курсором
    canvas.coords(images_id, event.x, event.y)

    # соединение элементов
    if len(images_id) == 2:
        element_id_1 = images_id[0]
        element_id_2 = images_id[1]
        element_1 = elements[element_id_1 - 1]
        element_2 = elements[element_id_2 - 1]

    # создаем новый елемент
    new_element = element_1 + element_2
    if new_element:
        if new_element not in elements:
            canvas.create_image(event.x, event.y, image= new_element.image)
            elements.append(new_element)


# создаем холст
canvas = Canvas(window,width=600,height=600)
canvas.pack()

# логика размещения базовых элементов
elements = [Earth(),Water(),Fire(),Wind()]
for elem in elements:
    canvas.create_image(randint(50,550),randint(50,550), image=elem.image)

# связываем нажатие мыши с функцией
window.bind('<B1-Motion>',move)



window.mainloop()