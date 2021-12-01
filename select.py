import psycopg2
import sqlalchemy
from pprint import pprint

database = sqlalchemy.create_engine('postgresql://postgres:dnweapons1513@localhost:5432/homework_db')
connection = database.connect()



if __name__ == '__main__':
    
    #название и год выхода альбомов, вышедших в 2018 году;
    
    select_albums = connection.execute("""SELECT  name, album_date FROM album WHERE album_date BETWEEN '2018-01-01' AND '2018-12-01';""").fetchall()
    
    pprint(select_albums)
    
    #название и продолжительность самого длительного трека;
    
    select_track = connection.execute("""SELECT name, duratation FROM track ORDER BY duratation DESC LIMIT 1;""").fetchall()
    
    pprint(select_track)
    
    #название треков, продолжительность которых не менее 3,5 минуты;
    
    select_max_track = connection.execute("""SELECT name FROM track WHERE duratation > 210;""").fetchall()
    pprint(select_max_track)
    
    #названия сборников, вышедших в период с 2018 по 2020 год включительно;
    select_collection = connection.execute("""SELECT name, date FROM collection WHERE date BETWEEN 2018 and 2020;""" ).fetchall()
    
    pprint(select_collection)
    
    #исполнители, чье имя состоит из 1 слова;
    select_name_one_word = connection.execute("""SELECT name FROM executor WHERE name not LIKE '%% %%';""").fetchall()
    
    pprint(select_name_one_word)
    
    #название треков, которые содержат слово "мой"/"my".
    select_track_name = connection.execute("""SELECT  name FROM track WHERE name LIKE '%%my%%'""").fetchall()
    
    pprint(select_track_name)
    
    
    
