# счетчик уникальных символов
import time
# создаем функцию
def count_sym(line):
    for sym in set(line):
        counter = 0
        for subsym in line:
            if sym == subsym:
                counter += 1
        print(sym,counter)


data = 'abcdefg' * 10000

# замеряем время с начала

start = time.time()
count_sym(data)
end = time.time()
print('время выполнения программы ',end - start)