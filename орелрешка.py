import random
storona = int(input("орел- 1, решка- 0  укажите выбранную сторону:"))
moneta = random.randint(0, 1)
if storona == moneta:
    print("вы выиграли")
else:
    print("вы проиграли")