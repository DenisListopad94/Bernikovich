import sqlite3

import db

conn = sqlite3.connect('path/to/database.db')
cursor = db.cursor()
cursor.execute('''
'CREATE TABLE"actors"(
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
"movie_fee" INTEGER)',
PRIMARY KEY("id" AUTOINCREMENT)
),
# создать колонку "fee_REAL" гонорары за фильм
ADD COLUMN fee_REAL INTEGER
#переименовать колонку "movie_fee" в "fee_actors", добавить колонку "city"
ADD COLUMN city TEXT
ALTER TABLE "actors"
RENAME COLUMN "movie_fee" TO "fee_actors"
INSERT INTO "actors"(name,surname,age,sex,movie_name,release,fee_REAL,fee_actors,city,director_name,director_surname,age_2,sex_2),
VALUES("Arnold","Schwarzenegger",75,"m","Terminator2",1991,102000000,1800000,"los Angeles","James","Cameron",68,"m")
      ("Bruce","Willis",67,"m","Die Hard",1988,25000000,1800000,"Los Angeles","John", "McTiernan",65,"m")
      ("Tom","Cruise",60,"m","Mission Impossible1",1996,80000000,1200000,"Los Angeles","Christopher","McQuarrie",65,"m")
      ("Brad","Pitt",53,"m","Rage",2014,68000000,1000000,"Los Angeles","David","Air",62,"m")
      ("Will","Smith",54,"m","I'm Legend",2007,65000000,1300000,"Los Angeles","Francis","Lawrence",63,"m")
      ("Leonardo","DiCaprio",48,"m","Titanic",1997,200000000,15000000,"Los Angeles","James","Cameron",68,"m")
      ("Tom","Hanks",66,"m","Catch me if you can",2002,52000000,15000000,"Los Angeles","Steven","Spielberg",75,"m")
      ("Johnny","Depp",59,"m","The Brave",1997,100000000,100000,"Los Angeles","Johnny","Depp",59,"m")
      ("Harrison","Ford",80,"m","Indiana Jones3",1989,48000000,1500000,"Los Angeles","Steven","Spielberg",75,"m")
      ("Sandra","Bullock",58,"f","Speed",1994,25000000,12000000,"Los Angeles","Jon","DeBont",79,"m")
      ("Halle","Berry",56,"f","Forest Gump",1994,55000000,1500000,"Los Angeles","Robert","Zemeckis",70,"m")
      ("Julia","Roberts",55,"f","Pretty Women",1990,1900000,1700000,"Los Angeles","Garry","Marshal",82,"m")
      ("Kate","Winslet",47,"f","Titanic",1997,200000000,15000000,"Los Angeles","James","Cameron",68,"m")
      ("Angelina","Jolie",47,"f","Lake House",2006,40000000,1700000,"Los Angeles","Alejandro","Agresti",61,"m")
# Вывести всех актёров которые снимались в период с 1990 по 2000 год. Актёры должны быть выведены только 1 раз.
SELECT DISTINCT name, surname
FROM actors
WHERE release BETWEEN 1990 AND 2000;
#Вывести все фильмы в которых приняли участие 2 и более актёра из нашей базы данных. Вывод организовать в порядке возрастания фамилий!
SELECT movie_name
FROM actors
GROUP BY movie_name
HAVING COUNT(name) >= 2;
#Вывести количество актёров мужского пола, которые есть в таблице которые старше 55 лет.
SELECT COUNT(*)
FROM actors
WHERE sex = "m" AND age > 55;
#Вывести всех актёров которые приняли участие в 2-х и более фильмах, которые есть а бд и которые имеют на своём счету 10000000$
SELECT COUNT(*)
FROM actors
WHERE sex = "m" AND age > 55;
#8.  Вывести общую сумму всех гонораров актёров в фильмах снятых в период с 1995 по 2005 год.
SELECT SUM(fee_REAL) as total_fee
FROM actors
WHERE release BETWEEN 1995 AND 2005;
#9.  Вывести фильмы и имена и фамилии актёров, которым на момент выпуска фильма в прокат было меньше 35 лет.
SELECT movie_name, name, surname
FROM actors
WHERE release - age < 35;
10.  Вывести все фильмы название которых состоит из 2 слов. Использовать регулярные выражения.
SELECT movie_name
FROM actors
WHERE movie_name REGEXP '^[A-Za-z]+ [A-Za-z]+$';
#.  Вывести  фильмы и общие выплаты актёрам. В порядке убывания общей суммы гонораров. Вывести первые 5 фильмов
SELECT movie_name, SUM(fee_REAL) as total_fee
FROM actors
GROUP BY movie_name
ORDER BY total_fee DESC
LIMIT 5;
#.  Вывести  фильм в котором приняло участие большее число актёров из вашей бд.
SELECT movie_name, COUNT(*) as actor_count
FROM actors
GROUP BY movie_name
ORDER BY actor_count DESC
LIMIT 1;
Ludmila Bernikovich, [22.03.2024 16:26]
SELECT name, surname
FROM all_people
WHERE (name, surname) NOT IN
(SELECT name, surname
FROM actors);
#.  Вывести все фильмы, а так же всех актёров кассовые сборы которых превысили 150000000.
SELECT movie_name, name, surname
FROM actors
WHERE movie_name IN
(SELECT movie_name
FROM actors
WHERE fee_REAL > 150000000);
#  Вывести всех режиссёров которые снимали фильмы до 2000 года. Режиссёры не должны повторятся
SELECT DISTINCT director_name, director_surname
FROM actors
WHERE "release" < 2000;
#6.  Добавить фильмы для актёров и режиссёров, у которых нет зависимости в таблице movies. Не забыть сделать изменения в таблице actors_movies.

INSERT INTO movies (movie_name, release)
VALUES ('Фильм 1', 2000),
       ('Фильм 2', 2001),
       ('Фильм 3', 1999);

#Затем мы можем выполнить операцию INSERT для добавления новых связей в таблицу actors_movies для актёров и режиссёров, у которых ещё нет зависимости:

INSERT INTO actors_movies (actor_id, movie_id)
SELECT a.id, m.id
FROM actors a, movies m
WHERE (a.name, a.surname) NOT IN
      (SELECT am.actor_name, am.actor_surname
       FROM actors_movies am)
      AND (a.director_name, a.director_surname) NOT IN
          (SELECT am.actor_name, am.actor_surname
           FROM actors_movies am);
#  Добавить колонку rating к фильмам. Задать значения рейтинга фильмов.
ALTER TABLE movies
ADD COLUMN rating INTEGER;

UPDATE movies
SET rating =
   CASE
      WHEN movie_name = 'Фильм 1' THEN 8
      WHEN movie_name = 'Фильм 2' THEN 7
      WHEN movie_name = 'Фильм 3' THEN 9
      ELSE NULL
   END;
#Вывести режиссёров и фильмы с рейтингом ниже среднего до 2000 года
SELECT director_name, director_surname, movie_name, rating
FROM actors
JOIN movies ON actors.movie_name = movies.movie_name
WHERE movies.release < 2000 AND movies.rating < (SELECT AVG(rating) FROM movies WHERE release < 2000);
#9.  Вывести всех актёров, которые знакомы с 2-мя и более другими актёрами.
SELECT actor_id, COUNT(*) AS num_actors_known
FROM actors_movies
GROUP BY actor_id
HAVING COUNT(*) >= 2;
# Вывести первых 5 самых высокооплачиваемых актёров
SELECT name, surname, fee_REAL
FROM actors
ORDER BY fee_REAL DESC
LIMIT 5
#.  Вывести всех режиссёров и актёров которые были задействованы только в 1 фильме
SELECT name, surname
FROM (
    SELECT name, surname, COUNT(DISTINCT movie_name) AS num_movies
    FROM actors
    GROUP BY name, surname
) AS actors_count
WHERE num_movies = 1;
#В поле finance таблицы bank_accounts внести информацию о доходах актёров. Доход считается с кассового сбора фильма. Если доход с фильма составил более 150000000 это 20%, от 150000000 до 100000000 – 15 %, если менее 100 миллионов 10%. Запрос на изменение таблицы bank_acounts должен быть выполнен с помощью подзапроса, который производит подсчёт суммы всех гонораров за фильмы
UPDATE bank_accounts
SET finance =
(
    SELECT SUM(
        CASE
            WHEN actors.fee_REAL > 150000000 THEN actors.fee_REAL * 0.2
            WHEN actors.fee_REAL <= 150000000 AND actors.fee_REAL > 100000000 THEN actors.fee_REAL * 0.15
            WHEN actors.fee_REAL <= 100000000 THEN actors.fee_REAL * 0.1
            ELSE 0
        END
    )
    FROM actors
    WHERE actors.name = bank_accounts.actor_name AND actors.surname = bank_accounts.actor_surname
);
##Затем можно выполнить запрос, чтобы найти людей, которые не участвовали в фильмах.
SELECT name, surname
FROM all_people
WHERE (name, surname) NOT IN
(SELECT DISTINCT director_name, director_surname
 FROM actors);
 #Добавить новое поле finance INTEGER в таблицу bank_accounts значение задать NULL.
ALTER TABLE bank_accounts
ADD COLUMN finance INTEGER DEFAULT NULL;
# Вывести первых 10  режиссёров, которые сняли высокобюджетные фильмы. Режиссёры не должны повторяться.
SELECT DISTINCT director_name, director_surname
FROM actors
WHERE fee_REAL > 10000000
LIMIT 10;
#  Вывести актёров и режиссёров, которые не участвовали не в одном из фильмов.

CREATE TABLE all_people AS
SELECT name, surname FROM actors
UNION
SELECT director_name AS name, director_surname as surname FROM actors;
''')
conn.close()
db.commit()