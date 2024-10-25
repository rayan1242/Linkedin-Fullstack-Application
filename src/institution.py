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
    try:
        no_of_employees = int(no_of_employees)
    except ValueError:
        print("Error: Number of employees must be an integer.")
        return

    if not isinstance(website, str) or not (website.startswith("http://") or website.startswith("https://")):
        print("Error: Website must be a string and start with 'http://' or 'https://'.")
        return

    if not isinstance(industry, str):
        print("Error: Industry must be a string.")
        return

    if not isinstance(name, str) or not name:
        print("Error: Name must be a non-empty string.")
        return

    if not isinstance(description, str):
        print("Error: Description must be a string.")
        return

    if not isinstance(location_city, str) or not location_city:
        print("Error: City must be a non-empty string.")
        return

    if not isinstance(location_state, str) or not location_state:
        print("Error: State must be a non-empty string.")
        return

    if not isinstance(location_country, str) or not location_country:
        print("Error: Country must be a non-empty string.")
        return
    try:
        query = """INSERT INTO institution (no_of_employees, website, industry, name, description, 
                   location_city, location_state, location_country) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (no_of_employees, website, industry, name, description, 
                  location_city, location_state, location_country)

        cursor.execute(query, values)
        connection.commit()
        institution_id = cursor.lastrowid

        print("\nInstitution created successfully with ID:", institution_id)
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    return institution_id

def read_institution(connection):
    cursor = connection.cursor(dictionary=True)

    institution_id = input("\nEnter institution ID: ")

    if not institution_id.isdigit():
        print("Error: Institution ID must be a numeric string.")
        return
    try:
        query = "SELECT * FROM institution WHERE institution_id = %s"
        cursor.execute(query, (institution_id,))
        result = cursor.fetchone()
        
        if result:
            print(tabulate([result], headers="keys", tablefmt="grid"))
        else:
            print("Institution not found")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    

def get_all_institutions(connection):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM institution"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        # Prepare the data for tabulate
        table_data = []
        for record in result:
            table_data.append([
                record['institution_id'],
                record['name'],
                record['no_of_employees'],
                record['website'],
                record['industry'],
                record['description'],
                record['location_city'],
                record['location_state'],
                record['location_country']
            ])

        # Print the table
        print(tabulate(table_data, headers=["institution_id", "name", "no_of_employees", "website", "industry", "description", "location_city", "location_state", "location_country"], tablefmt="grid"))
    else:
        print("No institution records found.")

    cursor.close()

def update_institution(connection):
    cursor = connection.cursor()
    
    institution_id = input("\nEnter institution ID to update: ")
    

    if(institution_id==""):
        print("Error: Institution ID cannot be empty.")
        return
    
    if not institution_id.isdigit():
        print("Error: Institution ID must be a numeric string.")
        return

    fields = ["no_of_employees", "website", "industry", "name", "description", 
              "location_city", "location_state", "location_country"]
    updates = []
    values = []
    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            if field == "no_of_employees":
                try:
                    value = int(value)
                except ValueError:
                    print("Error: Number of employees must be an integer.")
                    return
            elif field == "website":
                if not (value.startswith("http://") or value.startswith("https://")):
                    print("Error: Website must start with 'http://' or 'https://'.")
                    return
            elif field in ["industry", "name", "description", "location_city", "location_state", "location_country"]:
                if not isinstance(value, str):
                    print(f"Error: {field} must be a string.")
                    return
            updates.append(f"{field} = %s")
            values.append(value)

    if not updates:
        print("No fields to update")
        return
    try:
        query = f"UPDATE institution SET {', '.join(updates)} WHERE institution_id = %s"
        values.append(institution_id)

        cursor.execute(query, tuple(values))
        connection.commit()
        
        print("\nInstitution updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def delete_institution(connection):
    cursor = connection.cursor()
    
    institution_id = input("\nEnter institution ID to delete: ")
    
    if(institution_id==""):
        print("Error: Institution ID cannot be empty.")
        return
    
    if not institution_id.isdigit():
        print("Error: Institution ID must be a numeric string.")
        return
    
    try:
        query = "DELETE FROM institution WHERE institution_id = %s"
        cursor.execute(query, (institution_id,))
        connection.commit()
        print("\nInstitution deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def institution_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create institution")
        print("2: Read institution")
        print("3. Get all institution records")
        print("3: Update institution")
        print("4: Delete institution")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_institution(connection)
        elif choice == '2':
            read_institution(connection)           
        elif choice == '3':
            get_all_institutions(connection)
        elif choice == '4':
            update_institution(connection)
        elif choice == '5':
            delete_institution(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Institution Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
