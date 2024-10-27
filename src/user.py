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
        if len(name) < 2 or len(name) > 20:
            raise ValueError("Name must be between 2 and 20 characters")
    except ValueError as e:
        print(f"An error occurred: {e}")
    try:
        datetime.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Incorrect date format, should be YYYY-MM-DD")
    try:
        name = str(name)
    except ValueError:
        raise ValueError("Name must be a string")
    
    if not profile_pic.endswith(".jpg") and not profile_pic.endswith(".png") and not profile_pic.endswith(".jpeg"):
        raise ValueError("Profile picture URL must end with .jpg, .png, or .jpeg")

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

    # Prompt the user for the user ID and remove any leading/trailing whitespace
    user_id = input("Enter user ID: ")

    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
    if not user_id.isdigit():
        raise ValueError("User ID must be a digit")

    try:
        # Prepare the SQL query to select the user by user ID
        query = "SELECT * FROM user WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        result = cursor.fetchone()

        # Check if a result was found
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

    # Define the SQL query to select all users from the 'user' table
    query = "SELECT * FROM user"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        table_data = []

        # Iterate through each user in the result set
        for user in result:
            # Append user details to the table_data list
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

        # Print the user data in a formatted table using tabulate
        print(tabulate(table_data, headers=["user_id", "name", "dob", "age", "profile_pic", "location_city", "location_state", "location_country"], tablefmt="grid"))
       
    else:
        print("User not found")

    cursor.close()

# Update user
def update_user(connection):
    cursor = connection.cursor()

    # Prompt the user for the user ID to update
    user_id = input("\nEnter user ID to update: ")

    # Check if the user ID is empty
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
                # Ensure the profile picture URL starts with http:// or https://
                if not value.startswith("http://") and not value.startswith("https://"):
                    raise ("Profile picture URL must start with http:// or https://")
            elif field == "age":
                if not value.isdigit() or int(value) <= 0:
                    raise ValueError("Age must be a positive integer")
            updates.append(f"{field} = %s")
            values.append(value)

    if not updates:
        print("No fields to update")
        return

    try:
        # Construct the SQL update query
        query = f"UPDATE user SET {', '.join(updates)} WHERE user_id = %s"
        values.append(user_id)

        # Execute the update query
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

    # Prompt the user for the user ID to delete
    user_id = input("Enter user ID to delete: ")

    # Check if the user ID is empty
    if(user_id==""):
        print("Error: User ID cannot be empty.")
        return
    if not user_id.isdigit():
        raise ValueError("User ID must be a digit")

    try:
        query = "DELETE FROM user WHERE user_id = %s"
        # Execute the delete query with the provided user ID
        cursor.execute(query, (user_id,))
        connection.commit()
        print("User deleted successfully")
        
    except Exception as e:
        # Rollback in case of any error during deletion
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
