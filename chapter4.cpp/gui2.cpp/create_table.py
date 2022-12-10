import sqlite3
#connection to sqlite
#connection object
connection_obj = sqlite3.connect('arc.db')
#cursor_object
cursor_obj = connection_obj.cursor()
#drop the t1 table if already exists
cursor_obj.execute("DROP TABLE IF EXISTS t1")
#creating table

table = """ CREATE TABLE t1(
            email VARCHAR(255) NOT NULL,
            name CHAR(25) NOT NULL,
            score INT
);
"""
cursor_obj.execute(table)

connection_obj.execute(
   """INSERT INTO t1(email, name ,score) Values ("k1@gnail.com","k2",25)""")
connection_obj.execute(
   """INSERT INTO t1(email, name ,score) Values ("k2@gnail.com","k2",15)""")
connection_obj.execute(
   """INSERT INTO t1(email, name ,score) Values ("k3@gnail.com","k3",36)""")
connection_obj.execute(
   """INSERT INTO t1(email, name ,score) Values ("k4@gnail.com","k4",27)""")   
connection_obj.execute(
   """INSERT INTO t1(email, name ,score) Values ("k5@gnail.com","k5",40)""")
connection_obj.execute(
   """INSERT INTO t1(email, name ,score) Values ("k6@gnail.com","k6",36)""")
connection_obj.execute(
   """INSERT INTO t1(email, name ,score) Values ("k7@gnail.com","k7",27)""")

#Statement = '''SELECT* FROM t1'''
'''cursor_obj.execute(Statement)
print("ALL THE DATA")
output = cursor_obj.fetchall()
for row in output:
    print(row)'''


'''connection = sqlite3.connect('arc.db')
cursor = connection.cursor()'''

#WHERE CLAUSE TO RETRIEVE DATA
#cursor_obj.execute("SELECT * FROM t1 WHERE name = 'k2'")

# cursor = connection_obj.execute(
#     "select * from t1 order by name DESC")   # incresing order by show the value

#PRINTING THE CURSOR DATA
#print(cursor_obj.fetchall())

#Display data row by row
# for i in cursor:
#    print (i) 

cursor_obj.execute("Delete from t1 WHERE name = 'K3'")
connection_obj.commit()
connection_obj.close()    