import sqlite3

import db
from django.core.checks import database
conn = sqlite3.connect('tutorial.db')
cursor = conn.cursor()
with sqlite3.connect(db / database.db) as db:
    cursor = db.cursor()
cursor.execute('''
CREATE TABLE"actors"(
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
PRIMARY KEY("id" AUTOINCREMENT)
);
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
''')
conn.close()
db.commit()
