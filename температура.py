temp = int(input("введите температуру в градусах:"))
if temp < -10:
    print("очень холодно")
elif temp < 2:
    print("холодно")
elif temp < 12:
    print("прохладно")
elif temp < 18:
    print("тепло")
elif temp < 27:
    print("жарко")
else:
    print("очень жарко")