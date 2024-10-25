import mysql.connector
from tabulate import tabulate
from db import connect_to_database
from datetime import datetime

connection = connect_to_database()

def create_application(connection):
    cursor = connection.cursor()

    job_id = input("\nEnter job ID: ")
    user_id = input("Enter user ID: ")
    application_status = input("Enter application status: ")
    application_date = input("Enter application date (YYYY-MM-DD): ")

    if(job_id==""):
        print("Error: Job ID cannot be empty.")
        return
    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
    if(application_status==""):
        print("Error: Application status cannot be empty.")
        return
    if(application_date==""):
        print("Error: Application date cannot be empty.")
        return
    if not job_id.isdigit():
        print("Error: Job ID must be a number.")
        return
    if not user_id.isdigit():
        print("Error: User ID must be a number.")
        return
    try:
        application_date = datetime.strptime(application_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Application date must be in YYYY-MM-DD format.")
        return
    
    try:
        query = """INSERT INTO application (job_id, user_id, application_status, application_date)
                     VALUES (%s, %s, %s, %s)"""
        values = (job_id, user_id, application_status, application_date)
        cursor.execute(query, values)
        connection.commit()
        application_id = cursor.lastrowid
        print(f"Application created successfully with ID: {application_id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    return application_id


def read_application(connection):
    cursor = connection.cursor(dictionary=True)

    application_id = input("\nEnter application ID: ")
    
    if(application_id==""):
        print("Error: Application ID cannot be empty.")
        return
    if not application_id.isdigit():
        print("Error: Application ID must be a number.")
        return
    try:
        query = "SELECT * FROM application WHERE application_id = %s"
        cursor.execute(query, (application_id,))
        result = cursor.fetchone()
        if result:
            print(tabulate([result], headers="keys", tablefmt="grid"))
        else:
            print("Application not found")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def get_all_applications(connection):
    cursor = connection.cursor(dictionary=True)
    try:
        query = "SELECT * FROM application"
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(tabulate(result, headers="keys", tablefmt="grid"))
        else:
            print("No applications found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def update_application(connection):
    cursor = connection.cursor()

    application_id = input("\nEnter application ID to update: ")
    if(application_id==""):
        print("Error: Application ID cannot be empty.")
        return
    if not application_id.isdigit():
        print("Error: Application ID must be a number.")
        return
    
    fields = ["job_id", "user_id", "application_status", "application_date"]
    updates = []
    values = []
    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            if field in ["job_id", "user_id"]:
                if not value.isdigit():
                    print(f"Error: {field.replace('_', ' ').capitalize()} must be a number.")
                    return
            elif field == "application_date":
                try:
                    datetime.strptime(value, "%Y-%m-%d")
                except ValueError:
                    print("Error: Application date must be in YYYY-MM-DD format.")
                    return
            updates.append(f"{field} = %s")
            values.append(value)

    if not updates:
        print("\nNo fields to update")
        return
    try:
        query = f"UPDATE application SET {', '.join(updates)} WHERE application_id = %s"
        values.append(application_id)
        cursor.execute(query, tuple(values))
        connection.commit()
        print("\nApplication updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def delete_application(connection):
    cursor = connection.cursor()

    application_id = input("\nEnter application ID to delete: ")
   
    if(application_id==""):
        print("Error: Application ID cannot be empty.")
        return
    if not application_id.isdigit():
        print("Error: Application ID must be a number.")
        return
    try:
        query = "DELETE FROM application WHERE application_id = %s"
        cursor.execute(query, (application_id,))
        connection.commit()
        print("\nApplication deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def application_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create application")
        print("2: Read application")
        print("3. Get all application Records")
        print("3: Update application")
        print("4: Delete application")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_application(connection)
        elif choice == '2':
            read_application(connection)
        elif choice == '3':
            get_all_applications(connection)
        elif choice == '4':
            update_application(connection)
        elif choice == '5':
            delete_application(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Institution Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
