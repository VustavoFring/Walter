# алгебра логики
# 1 - истина,0-ложь
# 3 баз логические операции
# не(not) и(and) или(or)

# таблица истинности для (и) - логическое умножение

# таблица истинности для (или) - логическое сложение

# таблица истинности для (не) - логическое отрицание
# -----------------------------------------------------


# web - Scrapping на примере swapi
# подключаем библиотеку для запросов
import requests

# создаем функцию для персонажей 
def check_people(link):
    for i in range(1,6):
        data = requests.get(f'{link}/{i}').json()
        print(data['name'],data['mass'])   

def check_starships(link):
    for i in range(1,6):
        try:
            data = requests.get(f'{link}/{i}').json()
            print(data['name'])
        except KeyError:
            print('данные не найдены')   


# обьект для ссылки
url = 'https://swapi.dev/api/'
# создаем json обьект и создаем запрос к сайту

response = requests.get(url).json()
# получаем инфу о персонажах
people_api = response.get('people')
# получаем инфу о кораблях
starships_api = response.get('starships')
# получаем инфу о планетах
planet_api = response.get('planet')


# print(requests.get(people_api).json())
print(check_starships(starships_api))