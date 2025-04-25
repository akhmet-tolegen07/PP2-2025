import psycopg2
from psycopg2 import Error
import csv

try:
    connection = psycopg2.connect(
        dbname='postgres',
        user='postgres',
        password='AtuKereK34',
        host='localhost',
        port='5432'
    )
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Phonebooklab (
            name TEXT,
            phone TEXT
        );
    """)

    while True:
        print("""
        Select an action::
        1 — Load data from CSV
        2 — Enter data manually
        3 — Update name or number
        4 — Get data from table
        5 — Delete data
        6 — View with LIMIT and OFFSET
        0 — Exit
        """)
        action = int(input("Enter action number: "))

        if action == 0:
            print("Exiting the program...")
            break

        elif action == 1:
            with open('data.csv', 'r') as f:
                reader = csv.reader(f)
                next(reader)
                for row in reader:
                    cursor.execute("INSERT INTO Phonebooklab VALUES (%s, %s)", row)

        elif action == 2:
            print("How many people would you like to add?")
            n = int(input())
            for i in range(n):
                print("Enter name and phone number:")
                name1 = input()
                number1 = input()
                cursor.execute("INSERT INTO Phonebooklab (name, phone) VALUES (%s, %s)", (name1, number1))

        elif action == 3:
            print("What would you like to change? 1 - name, 2 - number")
            updatenum = int(input())
            if updatenum == 1:
                number1 = input("Enter the phone number you want to change the name of: ")
                name1 = input("Enter a new name: ")
                cursor.execute("UPDATE Phonebooklab SET name=%s WHERE phone=%s", (name1, number1))
                print("Name changed successfully.")
            elif updatenum == 2:
                name1 = input("Enter the name whose phone number you want to change: ")
                number1 = input("Enter a new phone number: ")
                cursor.execute("UPDATE Phonebooklab SET phone=%s WHERE name=%s", (number1, name1))
                print("The phone number has been changed successfully.")

        elif action == 4:
            print("1 - filter by name, 2 - by number, 3 - all records")
            option = int(input())
            if option == 1:
                name3 = input("Enter name: ")
                cursor.execute("SELECT * FROM Phonebooklab WHERE name=%s", (name3,))
                print(cursor.fetchall())
            elif option == 2:
                number3 = input("Enter phone number: ")
                cursor.execute("SELECT * FROM Phonebooklab WHERE phone=%s", (number3,))
                print(cursor.fetchall())
            elif option == 3:
                cursor.execute("SELECT * FROM Phonebooklab")
                print(cursor.fetchall())

        elif action == 5:
            print("Delete by: 1 - name, 2 - number")
            option = int(input())
            if option == 1:
                name4 = input("Enter your name: ")
                cursor.execute("DELETE FROM Phonebooklab WHERE name=%s", (name4,))
            elif option == 2:
                number4 = input("Enter phone number: ")
                cursor.execute("DELETE FROM Phonebooklab WHERE phone=%s", (number4,))

        elif action == 6:
            print("Enter LIMIT and OFFSET:")
            limit = int(input("LIMIT: "))
            offset = int(input("OFFSET: "))
            cursor.execute("SELECT * FROM Phonebooklab LIMIT %s OFFSET %s", (limit, offset))
            print(cursor.fetchall())

        connection.commit()

except (Exception, Error) as error:
    print("Error while working with PostgreSQL.", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("Connection to PostgreSQL closed.")
