import psycopg2
import csv


def insert_from_console():
    name = input("Your name: ")
    phone = input("Your phone number: ")
    conn = psycopg2.connect(
        dbname = 'PhoneBook',
        user = 'postgres',
        password = 'AtuKereK34',
        host = 'localhost',
        port = '5432'
    )
    cur = conn.cursor()
    insert_query = "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)"
    cur.execute(insert_query, (name, phone))

    conn.commit()
    cur.close()
    conn.close()
    print("Data is inputted")

def insert_from_csv(filename):
    try: 
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            next(reader)
            conn = psycopg2.connect(
                dbname = 'Phonebook',
                user = 'postgres',
                password = 'AtuKereK34',
                host = 'localhost',
                port = '5432'
            )
            cur = conn.cursor()
            for row in reader:
                if len(row) >= 2:
                    name,phone = row[0], row[1]
                    insert_query = "INSERT INTO PhoneBook (name, phone) VALUES (%s, %s)"

                    cur.execute(insert_query, (name,phone))
            conn.commit()
            cur.close()
            conn.close()
            print(f"Data from file {filename} is imported")
    except FileNotFoundError:
        print("File is not found")
    except Exception as e:
        print(f"Error: {e}")

def update_data():
    print("1. Change name")
    print("2. Change phone number")
    choice = input("What do you want?(1/2): ")

    conn = psycopg2.connect(
        dbname = 'PhoneBook',
        user = 'postgres',
        password = 'AtuKereK34',
        host = 'localhost',
        port = '5432'
    )
    cur = conn.cursor()

    if choice == '1':
        old_name = input("Enter current name: ")
        new_name = input("Enter new name: ")
        update_query = "UPDATE PhoneBook SET name = %s WHERE name = %s"
        params = (new_name, old_name)
    elif choice == '2':
        name = input("Enter your name: ")
        new_phone = input("Enter new phone number: ")
        update_query = "UPDATE PhoneBook SET phone = %s WHERE phone = %s"
        params = (new_phone, name)
    else:
        print("Incorrect choice")
        return
    try: 
        cur.execute(update_query, params)
        conn.commit()

        if cur.rowcount == 0:
            print("Record is not found")
        else:
            print("Data is updated")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
def query_data():
    print("1. Search by name")
    print("2. Search by phone number")
    print("3. Show all records")
    choice = input("What do you need?(1/2/3): ")

    conn = psycopg2.connect(
            dbname = 'PhoneBook',
            user = 'postgres',
            password = 'AtuKereK34',
            host = 'localhost',
            port = '5432'
        )
    cur = conn.cursor()
    
    if choice == '1':
        name = input("Enter name for searching: ")
        query = "SELECT * FROM PhoneBook WHERE name LIKE %s"
        params = (f"%{name}%",)
    elif choice == '2':
        phone = input("Enter phone number for searching: ")
        query = "SELECT * FROM PhoneBook WHERE phone LIKE %s"
        params = (f"%{phone}%",)
    elif choice == '3':
        query = "SELECT * FROM PhoneBook"
        params = ()
    else:
        print("Incorrect choice")
        return
    try:
        cur.execute(query, params)
        records = cur.fetchall()
        if not records:
            print("No records found")
        else:
            print("\nSearch results:")
            for row in records:
                print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
def delete_data():
    print("1. Delete by name")
    print("2. Delete by phone number")
    choice = input("How do you want to delete? (1/2): ")
    conn = psycopg2.connect(
            dbname = 'PhoneBook',
            user = 'postgres',
            password = 'AtuKereK34',
            host = 'localhost',
            port = '5432'
        )
    cur = conn.cursor()
    
    if choice == '1':
        name = input("Enter name to delete: ")
        delete_query = "DELETE FROM PhoneBook WHERE name = %s"
        params = (name,)
    elif choice == '2':
        phone = input("Enter phone number to delete: ")
        delete_query = "DELETE FROM PhoneBook WHERE phone = %s"
        params = (phone, )
    else:
        print("Incorrect choice")
        return
    try:
        cur.execute(delete_query, params)
        conn.commit()
        if cur.rowcount == 0:
            print("Record is not found")
        else:
            print(f"Deleted {cur.rowcount} record(s)")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        cur.close()
        conn.close()
def main_menu():
    while True:
        print("\nPhonebook Menu:")
        print("1. Insert data from console")
        print("2. Insert data from CSV file")
        print("3. Update data")
        print("4. Query data")
        print("5. Delete data")
        print("6. Exit")
        
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            insert_from_console()
        elif choice == '2':
            filename = input("Enter CSV filename: ")
            insert_from_csv(filename)
        elif choice == '3':
            update_data()
        elif choice == '4':
            query_data()
        elif choice == '5':
            delete_data()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
if __name__ == '__main__':
    main_menu()