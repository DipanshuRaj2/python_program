''' Sqlite = Database It is in-built  in phython for all the versions 2.5 ownwards
 import sqlite
 built up connection with database
 generate cursor = to fetch the data
 sqliteConnection = sqlite.connect('sql.db')(connect the database to phyton)
 Datatype  in Sqlite:
  NULL ,integer, Real, Text , blob(phython byte)'''


# check the version of sqlite
import sqlite3
   #Connect to Database and create a cursor
sqliteConnection = sqlite3.connect('sql.db') 
cursor = sqliteConnection.cursor() #default database se fetch kya hain
print ('DB Init 😊')

    #write a query and execute it with cursor
query ='select sqlite_version();'
cursor.execute(query)

    #fetch and output result
result = cursor.fetchall()
print('SQLite Version 🤨is {}'.format(result))

   #close the cursor
cursor.close()

#close DB connecction 
sqliteConnection.close()
print ('sqlite connection closed')

