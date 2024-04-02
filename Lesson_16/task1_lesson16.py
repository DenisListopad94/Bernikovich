import sqlite3

import db

conn = sqlite3.connect('path/to/database.db')
cursor = conn.cursor()
# создать таблицу "actors"
cursor.execute('''
    CREATE TABLE "actors" (
        "id" INTEGER NOT NULL UNIQUE,
        "name" TEXT NOT NULL,
        "surname" TEXT,
        "age" INTEGER,
        "sex" TEXT,
        "director_name" TEXT NOT NULL,
        "director_surname" TEXT,
        "age_2" INTEGER,
        "sex_2" TEXT,
        "movie_name" TEXT,
        "release" INTEGER,
        "movie_fee" INTEGER,
        "fee_REAL" INTEGER,
        "city" TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    )''')

# вставить данные в таблицу "actors"
cursor.execute('''
    INSERT INTO "actors" (
        name, surname, age, sex, movie_name, release, movie_fee, fee_REAL, city,
        director_name, director_surname, age_2, sex_2
    ) VALUES (
        "Arnold", "Schwarzenegger", 75, "m", "Terminator2", 1991, 102000000, 1800000,
        "Los Angeles", "James", "Cameron", 68, "m"
    ), (
        "Bruce", "Willis", 67, "m", "Die Hard", 1988, 25000000, 1800000,
        "Los Angeles", "John", "McTiernan", 65, "m"
    ), (
        "Tom", "Cruise", 60, "m", "Mission Impossible1", 1996, 80000000, 1200000,
        "Los Angeles", "Christopher", "McQuarrie", 65, "m"
    ), (
        "Brad", "Pitt", 53, "m", "Rage", 2014, 68000000, 1000000,
        "Los Angeles", "David", "Air", 62, "m"
    ), (
        "Will", "Smith", 54, "m", "I'm Legend", 2007, 65000000, 1300000,
        "Los Angeles", "Francis", "Lawrence", 63, "m"
    ), (
        "Leonardo", "DiCaprio", 48, "m", "Titanic", 1997, 200000000, 15000000,
        "Los Angeles", "James", "Cameron", 68, "m"
    ), (
        "Tom", "Hanks", 66, "m", "Catch me if you can", 2002, 52000000, 15000000,
        "Los Angeles", "Steven", "Spielberg", 75, "m"
    ), (
        "Johnny", "Depp", 59, "m", "The Brave", 1997, 100000000, 100000,
        "Los Angeles", "Johnny", "Depp", 59, "m"
    ), (
        "Harrison", "Ford", 80, "m", "Indiana Jones3", 1989, 48000000, 1500000,
        "Los Angeles", "Steven", "Spielberg", 75, "m"
    ), (
        "Sandra", "Bullock", 58, "f", "Speed", 1994, 25000000, 12000000,
        "Los Angeles", "Jon", "DeBont", 79, "m"
    ), (
        "Halle", "Berry", 56, "f", "Forest Gump", 1994, 55000000, 1500000,
        "Los Angeles", "Robert", "Zemeckis", 70, "m"
    ), (
        "Julia", "Roberts", 55, "f", "Pretty Women", 1990, 1900000, 1700000,
        "Los Angeles", "Garry", "Marshal", 82, "m"
    ), (
        "Kate", "Winslet", 47, "f", "Titanic", 1997, 200000000, 15000000,
        "Los Angeles", "James", "Cameron", 68, "m"
    ), (
        "Angelina", "Jolie", 47, "f", "Lake House", 2006, 40000000, 1700000,
        "Los Angeles", "Alejandro", "Agresti", 61, "m"
    )''')

# вывести все фильмы, которые были сняты с 2015 по 2020 год
cursor.execute('''
    SELECT movie_name
    FROM actors
    WHERE release >= 2015 AND release <= 2020
''')
movies = cursor.fetchall()
for movie in movies:
    print(movie[0])
#22.	Использую SQLite3 при помощи “сырого”  запроса вывести актёров и режиссёров, которые не участвовали не в одном из фильмов.

# вывести актёров, которые не участвовали в фильмах
cursor.execute('''
    SELECT name, surname
    FROM actors
    WHERE movie_name IS NULL
''')
actors = cursor.fetchall()
print("Актёры, которые не участвовали в фильмах:")
for actor in actors:
    print(f"{actor[0]} {actor[1]}")

# вывести режиссёров, которые не участвовали в фильмах
cursor.execute('''
    SELECT director_name, director_surname
    FROM actors
    WHERE movie_name IS NULL
''')
directors = cursor.fetchall()
print("\nРежиссёры, которые не участвовали в фильмах:")
for director in directors:
    print(f"{director[0]} {director[1]}")
#3.	Использую SQLite3 при помощи “сырого”  запроса вывести все фильмы  которые были сняты после 2000 года и в которых приняло участие более 1 актёра.
year = 2000
cursor.execute('SELECT movie_name FROM actors WHERE release > ?', (2000,))
movies = cursor.fetchall()

for movie in movies:
    print(movie[0])
 #4.	Использую SQLite3 при помощи “сырого”  запроса вывести первых 5 самых высокооплачиваемых актёров.
cursor.execute('''
     SELECT name, surname, feeREAL
     FROM actors
     ORDER BY feeREAL DESC
     LIMIT 5
 ''')
actors = cursor.fetchall()

print("Первые 5 самых высокооплачиваемых актеров:")
for actor in actors:
    print(f"{actor} {actor[1]} - {actor[2]}")
 #5.	Использую SQLite3 при помощи “сырого”  запроса вывести всех режиссёров и актёров которые были задействованы только в 1 фильме
cursor.execute('''
     SELECT directorname, directorsurname
     FROM actors
     GROUP BY directorname, directorsurname
     HAVING COUNT() = 1
 ''')
directors = cursor.fetchall()
print("Режиссеры, задействованные только в 1 фильме:")
for director in directors:
    print(f"{director[0]} {director[1]}")

cursor.execute('''
     SELECT name, surname
     FROM actors
     GROUP BY name, surname
     HAVING COUNT() = 1
 ''')
actors = cursor.fetchall()
print("\nАктеры, задействованные только в 1 фильме:")
for actor in actors:
    print(f"{actor} {actor[1]}")

conn.close()
db.commit()