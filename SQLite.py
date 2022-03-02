import sqlite3

#connect to the database
conn=sqlite3.connect('movies.db')

#create a cursor
c=conn.cursor()

#execute our command uing cursor
c.execute("SELECT * from movies")

c.execute("SELECT * from movies where Actor='George Clooney'")

#inbuilt function to fetch data of resultant queries
print(c.fetchall())

print("Code executed successfully..")

#commit our command
conn.commit()
#close our command
conn.close()
