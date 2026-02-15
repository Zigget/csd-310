"""
Samuel Sidzyik
Module 6.2
2/15/26

Create python code to run sql queries
"""

""" import statements """
import mysql.connector # to connect
from mysql.connector import errorcode
 
import dotenv # to use .env file
from dotenv import dotenv_values

#using our .env file
secrets = dotenv_values(".env")
 
""" database config object """
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
    cursor.execute("SELECT * FROM studio")
    Lines = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for Line in Lines:
        print(f"Studio ID: {Line[0]}\nStudio Name: {Line[1]}\n")

    cursor.execute("SELECT * FROM Genre")
    Lines = cursor.fetchall()
    print("-- DISPLAYING Genre RECORDS --")
    for Line in Lines:
        print(f"Genre ID: {Line[0]}\nGenre Name: {Line[1]}\n")

    cursor.execute("SELECT film_name, film_runtime FROM film WHERE film_runtime < 120")
    Lines = cursor.fetchall()
    print("-- DISPLAYING Short Film RECORDS --")
    for Line in Lines:
        print(f"Film Name: {Line[0]}\nRuntime: {Line[1]}\n")

    cursor.execute("SELECT film_name, film_director FROM film Order By film_director")
    Lines = cursor.fetchall()
    print("-- DISPLAYING Studio RECORDS --")
    for Line in Lines:
        print(f"Film Name: {Line[0]}\nDirector: {Line[1]}\n")

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