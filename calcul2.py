command = input('* / + -')
operations =['*','/','+','-']
с = 0
num_1 = input()
num_2 = input()

def calc():
    try:
        a = int(num_1)
    except:
        print('вы ввели недопустимый тип данных')
    try:
        b = int(num_2)
    except:
        print('вы ввели недопустимый тип данных')
    if command in operations:
            
        if command == '*':
            print(a*b)
        elif command == '/':
            print(a/b)
        elif command == '+':
            print(a+b)
        else:
            print(a-b)
    else:
        print('вы ввели недопустимую операцию')

calc()






