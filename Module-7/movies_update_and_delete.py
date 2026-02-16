"""
Samuel Sidzyik
Module 7.2
2/15/26

Create python code to run sql queries for insert, change and delete
"""

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")
 
""" database config object """
def main():

    config = {
        "user": secrets["USER"],
        "password": secrets["PASSWORD"],
        "host": secrets["HOST"],
        "database": secrets["DATABASE"],
        "raise_on_warnings": True #not in .env file
    }
    try:
        """ try/catch block for handling potential MySQL database errors """ 
    
        db = mysql.connector.connect(**config) # connect to the movies database 
        
        cursor = db.cursor()
        print("-- DISPLAYING FILMS --")
        PrintFilms(cursor)
        """ I didn't see the instruction not to use Star Wars until I was about to submit it....
        cursor.execute("INSERT INTO film (film_id,film_name,film_releaseDate,film_runtime,film_director,studio_id,genre_id)"\
                       "VALUES (4,'Star Wars',1977,121,'George Lucus',1,2);")
        """
        cursor.execute("INSERT INTO film (film_id,film_name,film_releaseDate,film_runtime,film_director,studio_id,genre_id)"\
                       "VALUES (4,'Cocaine Bear',2023,95,'Elizabeth Banks',3,1);")
        print("-- DISPLAYING FILMS AFTER INSERT --")
        PrintFilms(cursor)

        cursor.execute( "UPDATE film "\
                        "SET genre_id = 1 "\
                        "WHERE film_id = 2;")
        print("-- DISPLAYING FILMS AFTER UPDATE- Changed Alien to Horror --")
        PrintFilms(cursor)

        cursor.execute( "DELETE from film "\
                        "WHERE film_Name = 'Gladiator';")
        print("-- DISPLAYING FILMS AFTER DELETE--")
        PrintFilms(cursor)

    except mysql.connector.Error as err:
        """ on error code """
    
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")
    
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")
    
        else:
            print(err)
    
    finally:
        """ close the connection to MySQL """
    
        db.close()

def PrintFilms(cursor):
    cursor.execute( "SELECT f.film_name, f.film_director, s.studio_name, g.genre_name "\
                "FROM film as f "\
                "join studio as s on f.studio_id = s.studio_id "\
                "join genre as g on f.genre_id = g.genre_id;")
    Lines = cursor.fetchall()
    for Line in Lines:
        print(f"Film Name: {Line[0]}\n"\
            f"Director: {Line[1]}\n"\
            f"Genre Name: {Line[3]}\n"\
            f"Studio Name: {Line[2]}\n")
        
if __name__ == '__main__':
    main()