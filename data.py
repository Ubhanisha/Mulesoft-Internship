import sqlite3

#connect to the database
conn=sqlite3.connect('movies.db')

#create a cursor
c=conn.cursor()


#execute our command uing cursor

c.execute("INSERT into movies VALUES('Leonardo','Marion',2011,'Christopher Nolen')")
c.execute("INSERT into movies VALUES('George Clooney','Sandra Bullock',2013,'Alphonso')")
c.execute("INSERT into movies VALUES('Matt Damon','Jessica Chastain',2015,'Ridley Scott')")
c.execute("INSERT into movies VALUES('Christian Bale','Matt Damon',2019,'James Mangold')")

print("Code executed successfully..")

#commit our command
conn.commit()
#close our command
conn.close()