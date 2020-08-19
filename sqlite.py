import sqlite3

# Connection object to the database
conn = sqlite3.connect('users.db')

# Cursor object so SQL commands can be executed
cur = conn.cursor()

# Creating the database table
#cur.execute(''' CREATE TABLE users
#                (username text,
#                userclass text,
#                userrace text,
#                userside text)''')

# Inserting data into the table
cur.execute("INSERT INTO users VALUES ('Test','Test','Test','Test')")

# Commiting the changes
conn.commit()
 
# Gracefully closing the connection to the database
conn.close()
