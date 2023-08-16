n = int(input("введите количество чисел в последовательности:"))
numbers = []
correct_num = 0
for i in range(n):
    num = int(input("ваше число:"))
    numbers.append(num)
for i in numbers:
    if i%3 == 0 or i%7 == 0 or i%13 == 0:
        correct_num += 1
    else:
        correct_num += 0
if correct_num >= 3:
    print("удачная")
else:
    print("неуданая")