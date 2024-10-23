import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_job(connection):
    cursor = connection.cursor()

    institution_id = input("\nEnter institution ID: ")
    job_title = input("Enter job title: ")
    description = input("Enter description: ")
    job_type = input("Enter type: ")

    query = """INSERT INTO job (institution_id, job_title, description, type) 
               VALUES (%s, %s, %s, %s)"""
    values = (institution_id, job_title, description, job_type)

    cursor.execute(query, values)
    connection.commit()
    job_id = cursor.lastrowid

    print("\nJob created successfully with ID:", job_id)
    cursor.close()

    return job_id

def read_job(connection):
    cursor = connection.cursor(dictionary=True)

    job_id = input("\nEnter job ID: ")
    query = "SELECT * FROM job WHERE job_id = %s"

    cursor.execute(query, (job_id,))
    result = cursor.fetchone()

    if result:
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        print("\nJob not found")

    cursor.close()

def update_job(connection):
    cursor = connection.cursor()

    job_id = input("\nEnter job ID to update: ")
    fields = ["institution_id", "job_title", "description", "type"]
    updates = []
    values = []

    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            updates.append(f"{field} = %s")
            values.append(value)

    if not updates:
        print("\nNo fields to update")
        return

    query = f"UPDATE job SET {', '.join(updates)} WHERE job_id = %s"
    values.append(job_id)

    cursor.execute(query, tuple(values))
    connection.commit()

    print("\nJob updated successfully")

    cursor.close()

def delete_job(connection):
    cursor = connection.cursor()

    job_id = input("\nEnter job ID to delete: ")
    query = "DELETE FROM job WHERE job_id = %s"

    cursor.execute(query, (job_id,))
    connection.commit()

    print("\nJob deleted successfully")

    cursor.close()

def application_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create job")
        print("2: Read job")
        print("3: Update job")
        print("4: Delete job")
        print("0: Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == '1':
            create_job(connection)
        elif choice == '2':
            read_job(connection)
        elif choice == '3':
            update_job(connection)
        elif choice == '4':
            delete_job(connection)
        elif choice == '0':
            print("Database Disconnected Successfully!")
            print("\nExit from Experience Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
