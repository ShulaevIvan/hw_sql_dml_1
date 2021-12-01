import psycopg2
import sqlalchemy
from pprint import pprint

database = sqlalchemy.create_engine('postgresql://postgres:dnweapons1513@localhost:5432/homework_db')
connection = database.connect()



if __name__ == '__main__':

    #insert genre
    
    connection.execute("""INSERT INTO genre(id, name) 
                      VALUES(1,'pop');""")
    
    connection.execute("""INSERT INTO genre(id, name)
                      VALUES(2,'rock');""")
    
    connection.execute("""INSERT INTO genre(id, name)
                      VALUES(3,'blues');""")
    
    connection.execute("""INSERT INTO genre(id, name)
                      VALUES(4,'industrial');""")
    
    connection.execute("""INSERT INTO genre(id, name)
                      VALUES(5,'techno');""")
    
    #insert executor
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(1,'Alban Robinson');""")
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(2,'Arabella Morris');""")
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(3,'Chester');""")
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(4,'Rose Ryan');""")
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(5,'Samuel Osborne');""")
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(6,'Lionel Conley');""")
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(7,'Bryce Pitts');""")
    
    connection.execute("""INSERT INTO executor(id,name)
                      VALUES(8,'Blaise Tate');""")
    
    #insert references executor-genre
    
    connection.execute("""INSERT INTO executor_genre VALUES(1,1,1);""")
    
    connection.execute("""INSERT INTO executor_genre VALUES(2,2,2);""")
    
    connection.execute("""INSERT INTO executor_genre VALUES(3,3,3);""")
    
    connection.execute("""INSERT INTO executor_genre VALUES(4,4,4);""")
    
    connection.execute("""INSERT INTO executor_genre VALUES(5,5,5);""")
    
    #insert albums
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(1, 'boffin', '2017-05-08');""")
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(2, 'lyonia', '2020-05-11');""")
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(3, 'messrs', '2018-04-01');""")
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(4, 'rickey', '2018-09-01');""")
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(5, 'sandak', '2018-10-05');""")
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(6, 'unpray', '2021-02-01');""")
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(7, 'coecal', '2018-11-01');""")
    
    connection.execute("""INSERT INTO album(id, name, album_date)
                       VALUES(8, 'timing', '2019-04-15');""")
    
    #insert references executor-album
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(1,1,1);""")
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(2,2,2);""")
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(3,3,3);""")
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(4,4,4);""")
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(5,5,5);""")
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(6,2,1);""")
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(7,3,2);""")
    
    connection.execute("""INSERT INTO executor_album(id,album_id,executor_id) VALUES(8,4,1);""")
    
    #insert tracks
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(1,'test_track_1', 30.3, 1);""")
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(2,'test_track_2', 121.5, 2);""")
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(3,'test_track_3', 180, 3);""")
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(4,'test_track_4', 104.30, 4);""")
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(5,'test_track_5', 184.6, 5);""")
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(6,'my_test_track_6', 199, 6);""")
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(7,'test_track_my_7', 100, 7);""")
    
    connection.execute("""INSERT INTO track(id, name, duratation, album_id)
                                      VALUES(8,'test_track_8', 250, 8);""")
    #insert collections
    
    connection.execute("""INSERT INTO collection(id, name, date)
                                              VALUES(1, 'Fight For The Bills', 2019);""")
    
    connection.execute("""INSERT INTO collection(id, name, date)
                                              VALUES(2, 'Time Of My Life', 2018);""")
    
    connection.execute("""INSERT INTO collection(id, name, date)
                                              VALUES(3, 'Ministry For The Good Times', 2015);""")
    
    connection.execute("""INSERT INTO collection(id, name, date)
                                              VALUES(4, 'Altered And Future', 2019);""")
    
    connection.execute("""INSERT INTO collection(id, name, date)
                                              VALUES(5, 'Give It All You Got', 2021);""")
    
    #insert references collection-track
    
    connection.execute("""INSERT INTO track_collection(id, track_id, collection_id)
                                                   VALUES (1, 1, 1);""")
    
    connection.execute("""INSERT INTO track_collection(id, track_id, collection_id)
                                                   VALUES (2, 2, 2);""")
    
    connection.execute("""INSERT INTO track_collection(id, track_id, collection_id)
                                                   VALUES (3, 3, 3);""")
    
    connection.execute("""INSERT INTO track_collection(id, track_id, collection_id)
                                                   VALUES (4, 4, 4);""")
    
    connection.execute("""INSERT INTO track_collection(id, track_id, collection_id)
                                                   VALUES (5, 5, 5);""")
    
    
    
