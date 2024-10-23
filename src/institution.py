import mysql.connector
from tabulate import tabulate
from db import connect_to_database
connection = connect_to_database()

def create_institution(connection):
    cursor = connection.cursor()

    no_of_employees = input("\nEnter number of employees: ")
    website = input("Enter website: ")
    industry = input("Enter industry: ")
    name = input("Enter name: ")
    description = input("Enter description: ")
    location_city = input("Enter city: ")
    location_state = input("Enter state: ")
    location_country = input("Enter country: ")

    query = """INSERT INTO institution (no_of_employees, website, industry, name, description, 
               location_city, location_state, location_country) 
               VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
    values = (no_of_employees, website, industry, name, description, 
              location_city, location_state, location_country)

    cursor.execute(query, values)
    connection.commit()
    institution_id = cursor.lastrowid

    print("\nInstitution created successfully with ID:", institution_id)
    cursor.close()
    return institution_id

def read_institution(connection):
    cursor = connection.cursor(dictionary=True)

    institution_id = input("\nEnter institution ID: ")
    query = "SELECT * FROM institution WHERE institution_id = %s"
    
    cursor.execute(query, (institution_id,))
    result = cursor.fetchone()
    
    if result:
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        print("Institution not found")
    
    cursor.close()

def update_institution(connection):
    cursor = connection.cursor()
    
    institution_id = input("\nEnter institution ID to update: ")
    fields = ["no_of_employees", "website", "industry", "name", "description", 
              "location_city", "location_state", "location_country"]
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

    query = f"UPDATE institution SET {', '.join(updates)} WHERE institution_id = %s"
    values.append(institution_id)

    cursor.execute(query, tuple(values))
    connection.commit()
    
    print("\nInstitution updated successfully")
    cursor.close()

def delete_institution(connection):
    cursor = connection.cursor()
    
    institution_id = input("\nEnter institution ID to delete: ")
    query = "DELETE FROM institution WHERE institution_id = %s"
    
    cursor.execute(query, (institution_id,))
    connection.commit()
    
    print("\nInstitution deleted successfully")
    cursor.close()

def institution_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create institution")
        print("2: Read institution")
        print("3: Update institution")
        print("4: Delete institution")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_institution(connection)
        elif choice == '2':
            read_institution(connection)
        elif choice == '3':
            update_institution(connection)
        elif choice == '4':
            delete_institution(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Institution Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
