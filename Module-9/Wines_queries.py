"""
Girma Dingeto
Brady Heinz
Samuel Sidzyik
Module 9.1
3/1/26

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
 
    dbtables = ['delivery','department','distributor','distributororder',
                'distributororderline','distributorwine','employee',
                'inventorybalance','inventoryitem','location','suppliercontact',
                'supplierdelivery','suppliermaster','tank','timecard','vineyard',
                'vineyardblock','winedetails','winemaster']
    db = mysql.connector.connect(**config) # connect to the movies database 

    for table in dbtables:
        cursor = db.cursor()
        cursor.execute(f"SELECT * FROM {table}")
        Lines = cursor.fetchall()
        print(f"-- DISPLAYING {table.upper()} RECORDS --")
        columns = [col[0] for col in cursor.description]
        for Line in Lines:
            counter = 0
            for cols in columns:
                print(f"{cols}: {Line[counter]}")
                counter += 1
            exitchar = input(f"\nPress enter to coninue.\nType 't' to skip table.\nType 'q' to skip show data. > ")
            if exitchar.lower() == 'q' or exitchar.lower() == 't':
                break
        if exitchar.lower() == 'q':
            break

    cursor.execute("""select inventoryitem.ItemName, QuantityOnHand, UnitOfMeasure from winery.inventorybalance
                    join winery.inventoryitem on inventoryitem.itemID = inventorybalance.itemID
                    where QuantityOnHand < 300""")
    Lines = cursor.fetchall()
    print(f"\n-- DISPLAYING LOW INVENTORY --")
    for Line in Lines:
        print(f"Item: {Line[0]}\nRemaining: {Line[1]}\nUnit: {Line[2]}\n")

    cursor.execute("""SELECT concat(LastName,", ", FirstName) as "Name", WageRate FROM winery.employee
                   order by WageRate desc limit 2;""")
    Lines = cursor.fetchall()
    print(f"\n-- DISPLAYING HIGH VALUE EMPLOYEES --")
    for Line in Lines:
        print(f"\nName: {Line[0]}\nValue: {Line[1]}")



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