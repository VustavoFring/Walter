import sqlite3
from pprint import pprint

# создаем класс пользователя
class User:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender

# функция создания таблицы users
def create_table_users(cursor):

# настраимваем подключение к нашей бд
# пример создания sql запроса
    command = '''
    CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    name TEXT,
    surname TEXT,
    gender TEXT);
    '''
    # передаем курсору команду на исполнение
    cursor.execute(command)


# функция для добавления пользователя
def add_user(cursor, user):
    command = '''
    INSERT INTO users (name, surname, gender)
    VAlUES (?, ?, ?);
    '''
    # передаем курсору команду на исполнение
    cursor.execute(command,(user.name, user.surname, user.gender))

# функция вывода информации о всех пользователях

def get_users_list(cursor):
    command = '''
    SELECT *
    FROM users;
    '''
    result = cursor.execute(command)
    users_list = result.fetchall()

    for user in users_list:
        print(*user)

def get_user(cursor,users_id):
    command = '''
    SELECT *
    FROM users
    WHERE id = ?;
    '''
    result = cursor.execute(command,(users_id,))
    user = result.fetchall()
    print(*user)

# функция для обновления имени пользователя
def update_user_name(cursor, users_id, new_name):
    command = '''
    UPDATE users
    SET name = ?
    WHERE id = ?;
    '''
    result = cursor.execute(command,(new_name, users_id))

with sqlite3.connect('data.db') as cursor:
    # курсор - обьект с помощью которого будем выполнять sql запросы
    create_table_users(cursor)

    # добавляем новых пользователей
    # add_user(cursor, User(name='Ryan',surname='Gosling',gender='male'))
    # add_user(cursor, User(name='Robert',surname='Oppenheimer',gender='male'))
    # add_user(cursor, User(name='Walter',surname='White',gender='male'))
    # add_user(cursor, User(name='Jessy',surname='Pinkman',gender='male'))
    # get_users_list(cursor)
    get_user(cursor, 3)
    update_user_name(cursor, 3, 'Hisenberg')
    get_user(cursor, 3)
