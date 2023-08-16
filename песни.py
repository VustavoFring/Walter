songs = {

'Bad Guy': 3,

'Thunder': 3,

'Sweater Weather': 4,

'Numb': 3,

'Karma Police': 4,

'Enjoy the Silence': 4,

'Obstacles': 3,

'Crosses': 2,

'Unnamed Feeling': 7

}
n = int(input("введите количество желаемых песен(не больше 9):"))
summ_len = 0
for i in range(n):
    song = input("ваша песня:")
for i in range(n):
    lenght = songs[song]
    summ_len += lenght
print("общая длительность звучания ваших песен-",summ_len)

