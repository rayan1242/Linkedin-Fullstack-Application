import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_education(connection):
    cursor = connection.cursor()

    user_id = input("\nEnter User ID: ")
    institution_id = input("Enter Institution ID: ")
    start = input("Enter Start Date (YYYY-MM-DD): ")
    end = input("Enter End Date (YYYY-MM-DD): ")
    course = input("Enter Course: ")

    query = """INSERT INTO education (user_id, institution_id, start, end, course)
               VALUES (%s, %s, %s, %s, %s)"""
    values = (user_id, institution_id, start, end, course)

    cursor.execute(query, values)
    connection.commit()
    education_id = cursor.lastrowid

    print(f"\nEducation record created successfully with ID: {education_id}")
    cursor.close()

def read_education(connection):
    cursor = connection.cursor(dictionary=True)

    user_id = input("\nEnter User ID to retrieve education records: ")
    query = "SELECT * FROM education WHERE user_id = %s"

    cursor.execute(query, (user_id,))
    results = cursor.fetchall()

    if results:
        print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
        print("No education records found for this user.")

    cursor.close()

def update_education(connection):
    cursor = connection.cursor()

    education_id = input("Enter Education ID to update: ")
    fields = ["user_id", "institution_id", "start_date", "end_date", "course"]
    updates = []
    values = []

    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            updates.append(f"{field} = %s")
            values.append(value)

    if not updates:
        print("No fields to update")
        return

    query = f"UPDATE education SET {', '.join(updates)} WHERE id = %s"
    values.append(education_id)

    cursor.execute(query, tuple(values))
    connection.commit()

    print("\nEducation record updated successfully")
    cursor.close()

def delete_education(connection):
    cursor = connection.cursor()

    education_id = input("Enter Education ID to delete: ")
    query = "DELETE FROM education WHERE id = %s"

    cursor.execute(query, (education_id,))
    connection.commit()

    print(f"Education record with ID {education_id} deleted successfully")
    
    cursor.close()

def education_menu():
    connection = connect_to_database()

    if not connection:
        return

    while True:
        print("\nChoose an operation:")
        print("1: Create education record")
        print("2: Read education records")
        print("3: Update education record")
        print("4: Delete education record")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_education(connection)
        elif choice == '2':
            read_education(connection)
        elif choice == '3':
            update_education(connection)
        elif choice == '4':
            delete_education(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Education Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
