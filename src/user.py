from tabulate import tabulate
import datetime
from db import connect_to_database
connection = connect_to_database()

# Create user
def create_user(connection):
    cursor = connection.cursor()

    name = input("\nEnter Full Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    age = input("Enter Age: ")
    profile_pic = input("Enter Profile Picture URL: ")
    location_city = input("Enter City: ")
    location_state = input("Enter State: ")
    location_country = input("Enter Country: ")

    query = """INSERT INTO user (name, dob, age, profile_pic, location_city, location_state, location_country)
               VALUES (%s, %s, %s, %s, %s, %s, %s)"""
    values = (name, dob, age, profile_pic, location_city, location_state, location_country)

    cursor.execute(query, values)
    connection.commit()

    user_id = cursor.lastrowid
    print("\nUser created successfully with ID:", user_id)

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
def get_all_users(connection):
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

    user_id = input("\nEnter user ID to update: ")
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
    print("\nUser updated successfully")
    cursor.close()

# Delete user
def delete_user(connection):
    cursor = connection.cursor()

    user_id = input("Enter user ID to delete: ")
    query = "DELETE FROM user WHERE user_id = %s"
    cursor.execute(query, (user_id))
    connection.commit()

    print("User deleted successfully")

    cursor.close()

# Main function
def user_menu():
    connection = connect_to_database()

    while True:
        print("\nChoose an operation:")
        print("1: Create a New User.")
        print("2: Read an Existing User.")
        print("3: Update Existing user's Data.")
        print("4: Delete a User.")
        print("5: Get all Users.")
        print("0: Exit")

        choice = input("\nEnter your choice (0-5): ")

        if choice == '1':
            create_user(connection)
        elif choice == '2':
            read_user(connection)
        elif choice == '3':
            update_user(connection)
        elif choice == '4':
            delete_user(connection)
        elif choice == '5':
            get_all_users(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from User Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
            user_menu()
