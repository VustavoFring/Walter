# продвинутый калькулятор
while True:
    try:
        num_1 = int(input('введите первое число:'))
        oper = input('выбирайте операцию (+;-;*;/):')
        num_2 = int(input('введите второе число:'))
    except ValueError:
        print('были введены некоректные числа')
    else:
        if oper == '+':
            print('сумма равна:',num_1 + num_2)
        elif oper == '-':
            print('разность равна:',num_1 - num_2)
        elif oper == '*':
            print('произведение равно:',num_1 * num_2)
        elif oper == '/':
            try:
                print('частное от деления равно:',num_1/num_2)
            except ZeroDivisionError:
                print('делить на ноль нельзя!')
        else:
            print('ты выбрал другую операцию')
        cont_work = input('продолжить работу?(Y/N)')
        if cont_work == 'N':
            break
    finally:
        print('--------------------------------------')


# конструкция для обработки ошибок - try-except-else-finally

# try:
#     num_1 = int(input('введите первое число:'))
#     oper = input('выбирайте операцию (+;-;*;/):')
#     num_2 = int(input('введите второе число:'))
#     if oper == '/':
#         print(num_1/num_2)

# except ValueError:
#     print('произошла ошибка ввода числа!')
# except ZeroDivisionError:
#     print('делить на ноль нельзя!')
# except:
#     print('произошла неизвестная ошибка!')


# else:
#     print('квадрат числа',num_1**2)

# finally:
#     print('хорошего дня!')
