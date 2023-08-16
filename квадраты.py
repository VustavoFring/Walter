num1 = int(input('Введите первое число:'))**2
num2 = int(input('Введите второе число:'))**2
num3 = int(input('Введите третье число:'))**2
num4 = int(input('Введите четвертое число:'))**2
num5 = int(input('Введите пятое число:'))**2
numbers = [num1, num2, num3, num4, num5]
numbers.sort(reverse=1)
print('Квадраты введенных чисел(по убыванию)-',numbers)