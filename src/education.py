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

    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
    if(start==""):
        print("Error: Start date cannot be empty.")
        return
    if(course==""):
        print("Error: Course cannot be empty.")
        return 

    if (end!=""):  
        if start >= end:
            print("Error: Start date must be earlier than end date.")
            return

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
    
    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
        
    query = "SELECT * FROM education WHERE user_id = %s"

    cursor.execute(query, (user_id,))
    results = cursor.fetchall()

    if results:
        print(tabulate(results, headers="keys", tablefmt="grid"))
    else:
        print("No education records found for this user.")

    cursor.close()

def get_all_education(connection):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM education"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        # Prepare the data for tabulate
        table_data = []
        for record in result:
            table_data.append([
                record['user_id'],
                record['institution_id'],
                record['start'],
                record['end'],
                record['course']
            ])

        # Print the table
        print(tabulate(table_data, headers=["user_id", "institution_id", "start", "end", "course"], tablefmt="grid"))
    else:
        print("No education records found.")

    cursor.close()

def update_education(connection):
    cursor = connection.cursor()

    education_id = input("Enter Education ID to update: ")
    
    if(education_id==""):
        print("Error: Education ID cannot be empty.")
        return
    
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
    if(education_id==""):
        print("Error: Education ID cannot be empty.")
        return
    
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
        print("3. Get all education records")
        print("3: Update education record")
        print("4: Delete education record")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_education(connection)
        elif choice == '2':
            read_education(connection)
        elif choice == '3':
            get_all_education(connection)
        elif choice == '4':
            update_education(connection)
        elif choice == '5':
            delete_education(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Education Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
