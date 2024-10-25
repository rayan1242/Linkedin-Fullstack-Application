import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_skill(connection):
    cursor = connection.cursor()
    
    skill_name = input("\nEnter skill name: ")
    if not skill_name:
        print("Error: Skill name cannot be empty.")
        return
    try:
        query = "INSERT INTO skill (skill_name) VALUES (%s)"
        values = (skill_name,)
        cursor.execute(query, values)
        connection.commit()
        skill_id = cursor.lastrowid
        print(f"Skill created successfully with ID: {skill_id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    return skill_id

def read_skill(connection):
    cursor = connection.cursor(dictionary=True)

    skill_id = input("\nEnter skill ID: ")
    if not skill_id:
        print("Error: Skill ID cannot be empty.")
        return
    if not skill_id.isdigit():
        print("Error: Skill ID must be a number.")
        return
    try:
        query = "SELECT * FROM skill WHERE skill_id = %s"
        cursor.execute(query, (skill_id,))
        result = cursor.fetchone()
        if result:
            print(tabulate([result], headers="keys", tablefmt="grid"))
        else:
            print("Skill not found")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def get_all_skills(connection):
    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM skill"
        cursor.execute(query)
        result = cursor.fetchall()
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        result = []

    if result:
        # Prepare the data for tabulate
        table_data = []
        for record in result:
            table_data.append([
                record['skill_id'],
                record['skill_name']
            ])

        # Print the table
        print(tabulate(table_data, headers=["skill_id", "skill_name"], tablefmt="grid"))
    else:
        print("No skill records found.")

def update_skill(connection):
    cursor = connection.cursor()

    skill_id = input("\nEnter skill ID to update: ")
    if not skill_id:
        print("Error: Skill ID cannot be empty.")
        return
    if not skill_id.isdigit():
        print("Error: Skill ID must be a number.")
        return
    
    new_skill_name = input("Enter new skill name (leave blank to skip): ")

    if not new_skill_name:
        print("No fields to update")
        return
    try:
        query = "UPDATE skill SET skill_name = %s WHERE skill_id = %s"
        values = (new_skill_name, skill_id)
        cursor.execute(query, values)
        connection.commit()
        print("\nSkill updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def delete_skill(connection):
    cursor = connection.cursor()

    skill_id = input("\nEnter skill ID to delete: ")
    if not skill_id:
        print("Error: Skill ID cannot be empty.")
        return
    if not skill_id.isdigit():
        print("Error: Skill ID must be a number.")
        return
    try:
        query = "DELETE FROM skill WHERE skill_id = %s"
        cursor.execute(query, (skill_id,))
        connection.commit()
        print("\nSkill deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def skill_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create skill")
        print("2: Read skill")
        print("3. Get all skill records")
        print("4: Update skill")
        print("5: Delete skill")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_skill(connection)
        elif choice == '2':
            read_skill(connection)
        elif choice == '3':
            get_all_skills(connection)
        elif choice == '4':
            update_skill(connection)
        elif choice == '5':
            delete_skill(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Skill Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
