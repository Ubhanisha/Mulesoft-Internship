import sqlite3

#connect to the database
conn=sqlite3.connect('movies.db')

#create a cursor
c=conn.cursor()

#execute our command uing cursor
c.execute("""CREATE TABLE movies(
    #Actor text,Actress text,YearofRelease int,Director text)"""
)

print("Code executed successfully..")

#commit our command
conn.commit()
#close our command
conn.close()