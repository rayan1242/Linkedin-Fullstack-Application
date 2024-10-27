import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_experience(connection):
    cursor = connection.cursor()

    # Prompt the user for input values to create a new experience record
    user_id = input("\nEnter User ID: ")
    institution_id = input("Enter Institution ID: ")
    title = input("Enter Title: ")
    start = input("Enter Start Date (YYYY-MM-DD): ")
    end = input("Enter End Date (YYYY-MM-DD): ")
    description = input("Enter Description: ")

    # Validate User ID input
    if not user_id:
        print("Error: User ID cannot be empty.")
        return
    
    if not user_id.isdigit():
        print("Error: User ID must be a number.")
        return
    
    # Validate Institution ID input
    if not institution_id.isdigit():
        print("Error: Institution ID must be a number.")
        return
    if not title:
        print("Error: Title cannot be empty.")
        return 
    if not start:
        print("Error: Start date cannot be empty.")
        return
    if not description:
        print("Error: Description cannot be empty.")
        return
    if not user_id:
        print("Error: User ID cannot be empty.")
        return

    # Check if end date is provided for validation
    if(end==""):
        try:
            query = """INSERT INTO experience (user_id, institution_id, start, description, title)
                       VALUES (%s, %s, %s, %s, %s)"""
            values = (user_id, institution_id, start, description, title)
            cursor.execute(query, values)
            connection.commit()
            experience_id = cursor.lastrowid
            print(f"Experience created successfully with ID: {experience_id}")
        except mysql.connector.Error as err:
            print(f"Error: {err}")
        finally:
            cursor.close()
        return experience_id

    # Validate that start date is earlier than end date if end date is provided
    if(end!=""):
        if start >= end:
            print("Error: Start date must be earlier than end date.")
            return
    try:
        query = """INSERT INTO experience (user_id, institution_id, start, end, description, title)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (user_id, institution_id, start, end, description, title)
        cursor.execute(query, values)
        connection.commit()
        experience_id = cursor.lastrowid
        print(f"Experience created successfully with ID: {experience_id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    return experience_id

def read_experience(connection):
    cursor = connection.cursor(dictionary=True)

    # Prompt the user for the User ID to retrieve experiences
    user_id = input("\nEnter User ID to retrieve experiences: ")
    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return

    # Prepare the SQL query to select experiences for the given user_id
    query = "SELECT * FROM experience WHERE user_id = %s"

    cursor.execute(query, (user_id,))
    results = cursor.fetchall()

    # Check if any results were returned
    if results:
        print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
        print("No experiences found for this user.")

    cursor.close()

def get_all_experience(connection):
    cursor = connection.cursor(dictionary=True)

    # Prepare the SQL query to select all records from the experience table
    query = "SELECT * FROM experience"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        # Prepare the data for tabulate
        table_data = []
        for record in result:
            table_data.append([
                record['user_id'],
                record['institution_id'],
                record['title'],
                record['start'],
                record['end'],
                record['description']
            ])

        # Print the table
        print(tabulate(table_data, headers=["user_id", "institution_id", "title", "start", "end", "description"], tablefmt="grid"))
    else:
        print("No experience records found.")

    cursor.close()

def update_experience(connection):
    cursor = connection.cursor()

    # Prompt the user for the Experience ID to update
    exp_id = input("Enter Experience ID to update: ")
    
    # Validate that Experience ID is not empty
    if(exp_id==""):
        print("Error: Experience ID cannot be empty.")
        return  
    if not exp_id.isdigit():    
        print("Error: Experience ID must be a numeric string.")
        return  

    # Define the fields that can be updated    
    fields = ["user_id", "institution_id", "title", "company", "location", "start", "end", "description"]
    updates = []
    values = []

    # Loop through each field to prompt for new values
    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if field in ["user_id", "institution_id"] and value and not value.isdigit():
            print(f"Error: {field.replace('_', ' ').title()} must be a number.")
            return
        if field in ["start", "end"] and value:
            try:
                field.strptime(value, "%Y-%m-%d")
            except ValueError:
                print(f"Error: {field.replace('_', ' ').title()} must be in YYYY-MM-DD format.")
                return
        if value:
            updates.append(f"{field} = %s")
            values.append(value)

    # If no updates are provided, notify the user and exit
    if not updates:
        print("No fields to update")
        return
    try:
        query = f"UPDATE experience SET {', '.join(updates)} WHERE exp_id = %s"
        values.append(exp_id)

        cursor.execute(query, tuple(values))
        connection.commit()
        print("Experience updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def delete_experience(connection):
    cursor = connection.cursor()
    
    # Prompt the user for the Experience ID to delete
    exp_id = input("Enter Experience ID to delete: ")

    # Validate that Experience ID is not empty
    if(exp_id==""):
        print("Error: Experience ID cannot be empty.")
        return
        
    # Validate that Experience ID is a numeric string
    if not exp_id.isdigit():
        print("Error: Experience ID must be a numeric string.")
        return
    try:
        query = "DELETE FROM experience WHERE exp_id = %s"
        cursor.execute(query, (exp_id,))
        connection.commit()
        print(f"Experience with ID {exp_id} deleted successfully")  
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def experience_menu():
    connection = connect_to_database()

    if not connection:
        return

    while True:
        print("\nChoose an operation:")
        print("1: Create Experience")
        print("2: Read Experiences")
        print("3. Get All Experience Record")
        print("4: Update Experience")
        print("5: Delete Experience")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_experience(connection)
        elif choice == '2':
            read_experience(connection)
        elif choice == '3':
            get_all_experience(connection)
        elif choice == '4':
            update_experience(connection)
        elif choice == '5':
            delete_experience(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Experience Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
