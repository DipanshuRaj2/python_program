import sqlite3


connection = sqlite3.connect('arc.db')
cursor = connection.cursor()

table ="""CREATE TABLE STUDENT(
       NAME VARCHAR(34) , CLASS VARCHAR
         )"""


        

#WHERE CLAUSE TO RETRIEVE DATA
cursor.execute("SELECT * FROM STUDENT WHERE SECTION = 'B'")

#PRINTING THE CURSOR DATA
print(cursor.fetchall())

connection.commit()
connection.close()