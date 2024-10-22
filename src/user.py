import mysql.connector
from tabulate import tabulate
import datetime

# Establish database connection
def connect_to_database():
    return mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="root",
        database="linkedin"
    )

# Create user
def create_user(connection):
    cursor = connection.cursor()
    name = input("Enter name: ")
    dob = input("Enter date of birth (YYYY-MM-DD): ")
    profile_pic = input("Enter profile picture URL: ")
    location_city = input("Enter city: ")
    location_state = input("Enter state: ")
    location_country = input("Enter country: ")

    query = """INSERT INTO user (name, dob, profile_pic, location_city, location_state, location_country)
               VALUES (%s, %s, %s, %s, %s, %s)"""
    values = (name, dob, profile_pic, location_city, location_state, location_country)

    cursor.execute(query, values)
    connection.commit()
    user_id = cursor.lastrowid
    print("User created successfully with ID:", user_id)
    cursor.close()
    return user_id

# Read user
def read_user(connection):
    cursor = connection.cursor(dictionary=True)
    user_id = input("Enter user ID: ")
    query = "SELECT * FROM user WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    result = cursor.fetchone()
    if result:
        print(tabulate([result], headers="keys", tablefmt="grid"))
    else:
        print("User not found")
    cursor.close()


# Get all user
def get_all_user(connection):
    cursor = connection.cursor(dictionary=True)
    query = "SELECT * FROM user"
    cursor.execute(query)
    result = cursor.fetchall()
    if result:
        for user in result:
            print(f"ID: {user['user_id']}, Name: {user['name']}, DOB: {user['dob']}, "
              f"Profile Pic: {user['profile_pic']}, City: {user['location_city']}, "
              f"State: {user['location_state']}, Country: {user['location_country']}")
    else:
        print("User not found")
    cursor.close()

# Update user
def update_user(connection):
    cursor = connection.cursor()
    user_id = input("Enter user ID to update: ")
    fields = ["name", "dob", "profile_pic", "location_city", "location_state", "location_country"]
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

    query = f"UPDATE user SET {', '.join(updates)} WHERE user_id = %s"
    values.append(user_id)

    cursor.execute(query, tuple(values))
    connection.commit()
    print("User updated successfully")
    cursor.close()

# Delete user
def delete_user(connection):
    cursor = connection.cursor()
    user_id = input("Enter user ID to delete: ")
    query = "DELETE FROM user WHERE user_id = %s"
    cursor.execute(query, (user_id,))
    connection.commit()
    print("User deleted successfully")
    cursor.close()

# Main function
def main():
    connection = connect_to_database()
    print("Connected to the database successfully")
    
    while True:
        print("\nChoose an operation:")
        print("0: Create user")
        print("1: Read user")
        print("2: Update user")
        print("3: Delete user")
        print("4: Get all user")
        print("5: Exit")

        choice = input("Enter your choice (0-5): ")

        if choice == '0':
            create_user(connection)
        elif choice == '1':
            read_user(connection)
        elif choice == '2':
            update_user(connection)
        elif choice == '3':
            delete_user(connection)
        elif choice == '4':
            get_all_user(connection)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")

    connection.close()
    print("Goodbye!")

if __name__ == "__main__":
    main()