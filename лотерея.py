file = open('data.txt')
numbers = []
for line in file:
    numbers.append(int(line))
if sum(numbers) == max(numbers)*min(numbers):
    print('Повезло!')
else:
    print('В следующий раз')
