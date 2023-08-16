import random
n = int(input("введите кол-во чисел в списке:"))
numbers = []
for i in range(n):
    num = random.randint(-100, 100)
    numbers.append(num)
print(numbers,"- неотсортированный список")
numbers.sort()
print(numbers,"- отсортированный по возрастанию список")
