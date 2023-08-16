# # функции в программировании
# # def -  позволяет обЬявить функцию

# # использование функции позволяет не писать один и тот же код заново
# def get_sum(num):
#     s = 0
#     for i in range(1, num+1):
#         s += i
#     return s
# # return - позволяет вернуть значение в основное тело программы
# # за счет return мжно сохранить значение функции в переменную

# n = int(input())
# # вызываем функцию
# answer = get_sum(n)
# print(answer)

# работа с текстовыми файлами(.txt)
# взаимодействие с текстовыми файлами позволяет выгружать данные из файла или загружать в файл данные

# open() -позволяет открыть поток для взаимодействия с файлом

# по умолчанию файл открывается в режиме чтения
# r - read 
# file = open('data.txt','r')
# numbers = file.read()
# print(numbers) 

# w - режим записи 

# file = open('data.txt','w')
# file.write('21') # - записали в файл 21
# print(numbers)
# file.close()    

# считать ЧИСЛА 

file = open('data.txt')
numbers =[]
for line in file:
    numbers.append(int(line))
print(numbers)
