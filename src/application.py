import mysql.connector
from tabulate import tabulate
from db import connect_to_database
from datetime import datetime

connection = connect_to_database()

def create_application(connection):
    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Prompt user for application details
    job_id = input("\nEnter job ID: ")
    user_id = input("Enter user ID: ")
    application_status = input("Enter application status: ")
    application_date = input("Enter application date (YYYY-MM-DD): ")

    # Validate inputs   
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
    
    # Attempt to parse application_date to check format
    try:
        application_date = datetime.strptime(application_date, "%Y-%m-%d")
    except ValueError:
        print("Error: Application date must be in YYYY-MM-DD format.")
        return
    
    # Insert application into the database if all inputs are valid
    try:
        query = """INSERT INTO application (job_id, user_id, application_status, application_date)
                     VALUES (%s, %s, %s, %s)"""
        values = (job_id, user_id, application_status, application_date)

        # Execute the insert query
        cursor.execute(query, values)

        # Commit the transaction to save the application record
        connection.commit()
        application_id = cursor.lastrowid
        print(f"Application created successfully with ID: {application_id}")

    # Handle any database errors that occur during insertion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    return application_id


def read_application(connection):

    # Create a cursor with dictionary output to easily access column names
    cursor = connection.cursor(dictionary=True)

    # Prompt the user for the application ID to retrieve
    application_id = input("\nEnter application ID: ")
    
    # Validate that application_id is provided
    if(application_id==""):
        print("Error: Application ID cannot be empty.")
        return
    
    # Ensure application_id is numeric
    if not application_id.isdigit():
        print("Error: Application ID must be a number.")
        return
    
    # Execute a query to retrieve the application based on application_id
    try:
        query = "SELECT * FROM application WHERE application_id = %s"
        cursor.execute(query, (application_id,))
        result = cursor.fetchone()
        if result:
            print(tabulate([result], headers="keys", tablefmt="grid"))
        else:
            print("Application not found")

    # Handle any errors that may occur while interacting with the database
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    # Ensure the cursor is closed after the operation
    finally:
        cursor.close()


def get_all_applications(connection):
    # Create a cursor with dictionary output to format results as dictionaries
    cursor = connection.cursor(dictionary=True)

    # Attempt to retrieve all application records from the database
    try:
        query = "SELECT * FROM application"
        cursor.execute(query)
        result = cursor.fetchall()
        if result:
            print(tabulate(result, headers="keys", tablefmt="grid"))
        else:
            print("No applications found.")

    # Handle any errors that may occur during the database query execution
    except mysql.connector.Error as err:
        print(f"Error: {err}")

    # Ensure cursor is closed after completing the operation
    finally:
        cursor.close()


def update_application(connection):
    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    # Prompt the user for the application ID to update
    application_id = input("\nEnter application ID to update: ")
    if(application_id==""):
        print("Error: Application ID cannot be empty.")
        return
    if not application_id.isdigit():
        print("Error: Application ID must be a number.")
        return
    
    # Define fields that can be updated
    fields = ["job_id", "user_id", "application_status", "application_date"]
    updates = []
    values = []

    # Loop through each field and prompt the user for a new value
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

    # If no fields were updated, notify the user and exit
    if not updates:
        print("\nNo fields to update")
        return
    
    # Attempt to execute the update query
    try:
        query = f"UPDATE application SET {', '.join(updates)} WHERE application_id = %s"
        values.append(application_id)
        cursor.execute(query, tuple(values))
        connection.commit()
        print("\nApplication updated successfully")

    # Handle any database errors that occur during the update
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def delete_application(connection):
    # Create a cursor to execute SQL commands
    cursor = connection.cursor()

    application_id = input("\nEnter application ID to delete: ")

    # Validate that application_id is provided and is numeric
    if(application_id==""):
        print("Error: Application ID cannot be empty.")
        return
    if not application_id.isdigit():
        print("Error: Application ID must be a number.")
        return
    
    # Attempt to execute the delete query
    try:
        query = "DELETE FROM application WHERE application_id = %s"
        cursor.execute(query, (application_id,))
        connection.commit()
        print("\nApplication deleted successfully")

    # Handle any database errors that occur during the deletion
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def application_menu():
    # Establish a connection to the database
    connection = connect_to_database()
    
    # Loop to display the menu until the user chooses to exit
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
