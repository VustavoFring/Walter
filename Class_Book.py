class Book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year
    def get_title(self):
        self.title
    def get_author(self):
        self.author
    def get_year(self):
        self.year
        

book1 = Book('Трудно быть богом','Братья Стругацкие',1964)
book2 = Book('Евгений Онегин','Александр Пушкин',1833)
book3 = Book('Властелин Колец','Джон Рональд Руэл Толкин',1954)

print("Название: ",book1.title)
print("Автор:", book1.author)
print("Год издания:",book1.year)

print("Название: ",book2.title)
print("Автор:",book2.author)
print("Год издания:",book2.year)

print("Название: ",book3.title)
print("Автор:",book3.author)
print("Год издания:",book3.year)