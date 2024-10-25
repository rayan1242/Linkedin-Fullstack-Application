from tabulate import tabulate
import datetime
from db import connect_to_database
connection = connect_to_database()

# Create user
def create_user(connection):
    cursor = connection.cursor()

    name = input("\nEnter Full Name: ")
    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    profile_pic = input("Enter Profile Picture URL: ")
    location_city = input("Enter City: ")
    location_state = input("Enter State: ")
    location_country = input("Enter Country: ")

    if not dob or not profile_pic:
        print("Error: Date of Birth or Profile Picture URL cannot be empty.")
        return
    # Validate inputs
    try:
        datetime.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    try:
        name = str(name)
    except ValueError:
        raise ValueError("Name must be a string")
    
    if not profile_pic.startswith("http://") and not profile_pic.startswith("https://"):
        raise ValueError("Profile picture URL must start with http:// or https://")

    if not name or not location_city or not location_state or not location_country:
        raise ValueError("Name, city, state, and country cannot be empty")

    try:
        query = """INSERT INTO user (name, dob, profile_pic, location_city, location_state, location_country)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (name, dob, profile_pic, location_city, location_state, location_country)

        cursor.execute(query, values)
        connection.commit()

        user_id = cursor.lastrowid
        print("\nUser created successfully with ID:", user_id)
    except Exception as e:
        connection.rollback()
        print(f"An error occurred: {e}")
    finally:
        cursor.close()
    return user_id

# Read user
def read_user(connection):
    cursor = connection.cursor(dictionary=True)

    user_id = input("Enter user ID: ")

    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
    if not user_id.isdigit():
        raise ValueError("User ID must be a digit")

    try:
        query = "SELECT * FROM user WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        if result:
            print(tabulate([result], headers="keys", tablefmt="grid"))
        else:
            print("User not found")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        cursor.close()



# Get all user
def get_all_users(connection):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM user"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        table_data = []
        for user in result:
            table_data.append([
                user['user_id'],
                user['name'],
                user['dob'],
                user['age'],  
                user['profile_pic'],
                user['location_city'],
                user['location_state'],
                user['location_country']
            ])

        print(tabulate(table_data, headers=["user_id", "name", "dob", "age", "profile_pic", "location_city", "location_state", "location_country"], tablefmt="grid"))
       
    else:
        print("User not found")

    cursor.close()

# Update user
def update_user(connection):
    cursor = connection.cursor()

    user_id = input("\nEnter user ID to update: ")
    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
    if not user_id.isdigit():
        raise ValueError("User ID must be a digit")

    fields = ["name", "dob", "profile_pic", "location_city", "location_state", "location_country"]
    updates = []
    values = []

   
    # Validate and update fields
    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            if field == "dob":
                try:
                    datetime.datetime.strptime(value, '%Y-%m-%d')
                except ValueError:
                    raise ValueError("Incorrect date format, should be YYYY-MM-DD")
            elif field == "profile_pic":
                if not value.startswith("http://") and not value.startswith("https://"):
                    raise ValueError("Profile picture URL must start with http:// or https://")
            elif field == "age":
                if not value.isdigit() or int(value) <= 0:
                    raise ValueError("Age must be a positive integer")
            updates.append(f"{field} = %s")
            values.append(value)

    if not updates:
        print("No fields to update")
        return

    try:
        query = f"UPDATE user SET {', '.join(updates)} WHERE user_id = %s"
        values.append(user_id)
        cursor.execute(query, tuple(values))
        connection.commit()
        print("\nUser updated successfully")
    except Exception as e:
        connection.rollback()
        print(f"An error occurred: {e}")
    finally:
        cursor.close()

# Delete user
def delete_user(connection):
    cursor = connection.cursor()

    user_id = input("Enter user ID to delete: ")

    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
    if not user_id.isdigit():
        raise ValueError("User ID must be a digit")

    try:
        query = "DELETE FROM user WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        connection.commit()
        print("User deleted successfully")
    except Exception as e:
        connection.rollback()
        print(f"An error occurred: {e}")
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
