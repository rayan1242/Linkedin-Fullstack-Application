import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_skill(connection):
    cursor = connection.cursor()

    skill_name = input("\nEnter skill name: ")
    query = "INSERT INTO skill (skill_name) VALUES (%s)"
    values = (skill_name,)

    cursor.execute(query, values)
    connection.commit()
    skill_id = cursor.lastrowid

    print("\nSkill created successfully with ID:", skill_id)
    cursor.close()

    return skill_id

def read_skill(connection):
    cursor = connection.cursor(dictionary=True)

    skill_id = input("\nEnter skill ID: ")
    query = "SELECT * FROM skill WHERE skill_id = %s"

    cursor.execute(query, (skill_id,))
    result = cursor.fetchone()

    if result:
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        print("\nSkill not found")

    cursor.close()

def update_skill(connection):
    cursor = connection.cursor()

    skill_id = input("\nEnter skill ID to update: ")
    new_skill_name = input("Enter new skill name (leave blank to skip): ")

    if not new_skill_name:
        print("No fields to update")
        return

    query = "UPDATE skill SET skill_name = %s WHERE skill_id = %s"
    values = (new_skill_name, skill_id)

    cursor.execute(query, values)
    connection.commit()

    print("\nSkill updated successfully")

    cursor.close()

def delete_skill(connection):
    cursor = connection.cursor()

    skill_id = input("\nEnter skill ID to delete: ")
    query = "DELETE FROM skill WHERE skill_id = %s"

    cursor.execute(query, (skill_id,))
    connection.commit()

    print("\nSkill deleted successfully")

    cursor.close()

def skill_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create skill")
        print("2: Read skill")
        print("3: Update skill")
        print("4: Delete skill")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_skill(connection)
        elif choice == '2':
            read_skill(connection)
        elif choice == '3':
            update_skill(connection)
        elif choice == '4':
            delete_skill(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Skill Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
