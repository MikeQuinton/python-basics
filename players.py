'''
File name: main.py
Author / Maintainer: Michael Quinton
Email: Michael@Quinton.io
Status: Production
Version: 0.1
'''

# Importing the SQLite3 module

import sqlite3

# Creating connection to SQLite database and cursor, used to loop through the table and manage data

conn = sqlite3.connect('users.db')
cur = conn.cursor()


# Declaring functions

def create_user():

    # Added for debugging purposes
    
    global name_match
    
    print("\nWe can now create a character, please enter your chosen stats\n")
    
    user_name = input("Enter a username: ")
    cur.execute("SELECT username FROM users WHERE username = (?);", (user_name,))
    name_match = cur.fetchall()

    try:
        join_match = "".join(name_match[0])

        if user_name == join_match:
            print(f"{user_name} is already in use, please choose a different username")
            create_user()
    except IndexError as IndexErr:
        print("{user_name} cannot be found within the index")
    user_race = input("Enter a race: ")
    user_side = input("Enter a side: ")

    # Executing SQL commands and then committing the changes to the database

    cur.execute("INSERT INTO users VALUES (?, ?, ?, ?);", (user_name, user_class, user_race, user_side))
    conn.commit()

    return "\nUser has been created successfully"


def remove_user():

    name = input("\nEnter a name to remove: ")
    cur.execute("DELETE FROM users WHERE username = (?);", (name,))

    conn.commit()

    return f"\n{name} has been successfully removed"


def display_characters():

    cur.execute("SELECT * FROM users")
    rows = cur.fetchall()
    for row in rows:
        row = f"\nUsername: {row[0]}\nClass: {row[1]}\nRace: {row[2]}\nSide: {row[3]}"
        print(row)


# Main loop
while True:

    try:
        option = int(input("""

1) Create a character
2) Remove a character
3) Display all characters

Please enter a choice: """))

    except ValueError as err:
        print("\nInvalid option, please choose from the main menu")
        continue

    if option == 1:
        print(create_user())

    elif option == 2:
        print(remove_user())

    elif option == 3:
        print(display_characters())

    elif option == 4:
        break

