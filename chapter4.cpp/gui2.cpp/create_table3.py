import sqlite3

connection =sqlite3.connect('arc.db')
cursor = connection.cursor()



# Display data inserted
print("EMPLOYEE TABLE: ")
data = cursor.execute('''SELECT * from employee''')
for row in data:
    print (row)

#updating
cursor.execute('''UPDATE EMPLOYEE SET INCOME = 5000 WHERE Age<25;''')    
print('\nAfter Updating...\n') 

#display data
print("EMPLOYEE Table: ")
data = cursor.execute('''select * from employee''')
for row in data  :
    print(row)

#Commit your changes in the database
conn.commit ()    