import mysql.connector
from tabulate import tabulate

def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="linkedin"
    )

def create_institution(connection):
    cursor = connection.cursor()
    no_of_employees = input("Enter number of employees: ")
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
    print("User created successfully with ID:", institution_id)
    cursor.close()
    return institution_id

def read_institution(connection):
    cursor = connection.cursor(dictionary=True)
    institution_id = input("Enter institution ID: ")
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
    institution_id = input("Enter institution ID to update: ")
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
    print("Institution updated successfully")
    cursor.close()

def delete_institution(connection):
    cursor = connection.cursor()
    institution_id = input("Enter institution ID to delete: ")
    query = "DELETE FROM institution WHERE institution_id = %s"
    cursor.execute(query, (institution_id,))
    connection.commit()
    print("Institution deleted successfully")
    cursor.close()

def main():
    connection = connect_to_database()
    print("Connected to the database successfully")
    
    while True:
        print("\nChoose an operation:")
        print("0: Create institution")
        print("1: Read institution")
        print("2: Update institution")
        print("3: Delete institution")
        print("4: Exit")

        choice = input("Enter your choice (0-4): ")

        if choice == '0':
            create_institution(connection)
        elif choice == '1':
            read_institution(connection)
        elif choice == '2':
            update_institution(connection)
        elif choice == '3':
            delete_institution(connection)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()