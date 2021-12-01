import psycopg2
import sqlalchemy
from pprint import pprint


database = sqlalchemy.create_engine('postgresql://postgres:dnweapons1513@localhost:5432/homework_db')
connection = database.connect()



if __name__ == '__main__':
    database = sqlalchemy.create_engine('postgresql://postgres:dnweapons1513@localhost:5432/homework_db')
    connection = database.connect()
    
    # connection.execute("""DROP TABLE genre;""")
    # connection.execute("""DROP TABLE executor;""")
    # connection.execute("""DROP TABLE album;""")
    # connection.execute("""DROP TABLE executor_album;""")
    # connection.execute("""DROP TABLE track;""")
    # connection.execute("""DROP TABLE track_collection;""")
    # connection.execute("""DROP TABLE executor_genre;""")
    
    connection.execute("""CREATE TABLE IF NOT EXISTS genre (
        id serial primary key,
        name varchar(40));
        """)
    
    connection.execute("""CREATE TABLE IF NOT EXISTS executor_genre (
        id serial primary key,
        genre_id integer not null references genre(id),
        executor_id integer not null references executor(id));
        """)
    
    connection.execute("""CREATE TABLE IF NOT EXISTS genre (
        id serial primary key,
        name varchar(40));
        """)
    
    connection.execute("""CREATE TABLE IF NOT EXISTS album (
        id serial primary key,
        name varchar(40),
        album_date date);
        """)
    
    connection.execute("""CREATE TABLE IF NOT EXISTS executor_album (
        id serial primary key,
        date date,
        album_id integer not null references album(id),
        executor_id integer not null references executor(id));
        """)
    
    connection.execute("""CREATE TABLE IF NOT EXISTS track (
        id serial primary key,
        name varchar(40),
        duratation numeric,
        album_id serial unique not null references album(id));
        """)
    
    connection.execute("""CREATE TABLE IF NOT EXISTS collection (
        id serial primary key,
        name varchar(40),
        date integer);
        """)
    
    connection.execute("""CREATE TABLE IF NOT EXISTS track_collection (
        id serial primary key,
        track_id integer not null references track(id),
        collection_id integer not null references collection(id));
        """)