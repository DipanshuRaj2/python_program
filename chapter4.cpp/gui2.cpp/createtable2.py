import sqlite3
#connection to sqlite
#connection object
connection_obj = sqlite3.connect('arc.db')
#cursor_object
cursor_obj = connection_obj.cursor()
#drop the t1 table if already exists
cursor_obj.execute("DROP TABLE IF EXISTS t2")
#creating table

table ="""CREATE TABLE t2(
Name varchar(255),
Class varchar(50),
Section varchar(45)
);"""
connection_obj.execute(table)
connection_obj.execute(
     """INSERT INTO t2(Name, Class, Section) VALUES("lol1","k1",k21ELA)""")
connection_obj.execute(
     """INSERT INTO t2(Name, Class, Section) VALUES("lol2","k2",k21ELA1)""")
connection_obj.execute(
     """INSERT INTO t2(Name, Class, Section) VALUES("lol3","k3",k21ELA2)""")
connection_obj.execute(
     """INSERT INTO t2(Name, Class, Section) VALUES("lol4","k4",k21ELA3)""")
connection_obj.execute(
     """INSERT INTO t2(Name, Class, Section) VALUES("lol5","k5",k21ELA4)""")
Statement ='''SELECT * FROM t2'''
cursor_obj.execute(Statement)
print("ALL THE DATA")
output = cursor_obj.fetchall()
for row in output:
    print(row)