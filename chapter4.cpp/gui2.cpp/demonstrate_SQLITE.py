#Phython3 program to Demonstrate SQlite3 datatypes
#create connection to database
import sqlite3

#create connection to database
cnt = sqlite3.connect('gfg.db')
cnt.execute('''drop table if exists exam_hall''')

#Create a exam_hall relation
cnt.execute('''CREATE TABLE exam_hall(
    name text,
    pin integer,
    occupancy real
);''')

#insert tuples for the relation 
cnt.execute('''
INSERT INTO exam_hall VALUES('center-a', 1148, 78.5)''')

cnt.execute('''INSERT INTO exam_hall VALUES(NULL, 1343, 898.3)''')

#Query the data, print the data and its type
cursor = cnt.execute('''SELECT * FROM exam_hall;''')
for i in cursor:
    print(str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]))
    print(str(type(i[0])) + ' ' + str(type(i[1])) + ' ' + str(type(i[2])))