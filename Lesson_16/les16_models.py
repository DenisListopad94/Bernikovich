
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Users(Base):
    __tablename__ = 'Users'

    id = Column(Integer, primary_key=True)
    first_name = Column(String(50))
    last_name = Column(String(50))
    age = Column(Integer)

#2. Создайте "движок" для подключения к базе данных SQLite и создайте таблицу через Base.metadata.create_all(engine):

from sqlalchemy import create_engine
import sqlite3
engine = create_engine('sqlite:///path/to/database.db')
Base.metadata.create_all(engine)


# Создаем подключение к базе данных
conn = sqlite3.connect('path/to/database.db')

# Создаем курсор для выполнения SQL-запросов
cursor = conn.cursor()

# Создаем таблицу "Users"
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER PRIMARY KEY,
        first_name TEXT(50),
        last_name TEXT(50),
        age INTEGER
    )
''')
conn.close()
conn.commit()
#7.	Создать сессию и добавить в базу 5 разных пользователей.
users = [
    (1, 'John', 'Doe', 30),
    (2, 'Alice', 'Smith', 25),
    (3, 'Michael', 'Johnson', 35),
    (4, 'Emma', 'Williams', 28),
    (5, 'David', 'Brown', 32)
]
cursor.executemany('INSERT INTO Users VALUES (?, ?, ?, ?)', users)
conn.close()
conn.commit()
#8.	Создать сессию и вывести первых 3 пользователей отсортированных по убыванию возроста
cursor.execute('SELECT * FROM Users ORDER BY age DESC LIMIT 3')
users = cursor.fetchall()

# Выводим результаты
for user in users:
    print(user)
conn.close()
conn.commit()
#9.	Создать сессию и вывести  пользователей по имени “Jhon”
with conn:
    # Выполняем SQL-запрос, который выбирает пользователей с указанным именем
    cursor.execute('SELECT * FROM Users WHERE first_name = ?', ('Jhon',))
    users = cursor.fetchall()

    # Выводим результаты
    for user in users:
        print(user)
conn.close()
conn.commit()
#Создать сессию и вывести  пользователей  старше 20 лет, а также в фамилии которых есть буква “a”. Отсортировать по убыванию фамилии.
with conn:
 cursor.execute('''
       SELECT * 
       FROM Users 
       WHERE age > 20 AND last_name LIKE '%a%'
       ORDER BY last_name DESC
   ''')
users = cursor.fetchall()

# Выводим результаты
for user in users:
    print(user)
conn.close()
conn.commit()
#2.	Создать сессию и вывести  пользователей от 10 до 20 лет, а также всех тех кому 30 лет.
with conn:
    cursor.execute('''
         SELECT * 
         FROM Users 
         WHERE age BETWEEN 10 AND 20 OR age = 30
     ''')
    users = cursor.fetchall()

    # Выводим результаты
    for user in users:
        print(user)
conn.close()
conn.commit()
#3.	Создать миграцию через alembic, настроив файлы ini и .env



