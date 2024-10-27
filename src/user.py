from tabulate import tabulate
import datetime
from db import connect_to_database
connection = connect_to_database()

# Create user
def create_user(connection):
    cursor = connection.cursor(dictionary=True)
    
    name = input("\nEnter Full Name: ")
    try:
        if len(name) < 2 or len(name) > 20:
            raise ValueError("Name must be between 2 and 20 characters")
    except ValueError as e:
        print(f"An error occurred: {e}")
        return

    dob = input("Enter Date of Birth (YYYY-MM-DD): ")
    if not dob:
        print("Error: Date of Birth cannot be empty.")
        return
    try:
        datetime.datetime.strptime(dob, '%Y-%m-%d')
    except ValueError:
        print("Incorrect date format, should be YYYY-MM-DD")
        return

    profile_pic = input("Enter Profile Picture URL: ")
    if not profile_pic:
        print("Error: Profile Picture URL cannot be empty.")
        return
    if not profile_pic.endswith(".jpg") and not profile_pic.endswith(".png") and not profile_pic.endswith(".jpeg"):
        print("Profile picture URL must end with .jpg, .png, or .jpeg")
        return

    location_city = input("Enter City: ")
    if not location_city:
        print("Error: City cannot be empty.")
        return

    location_state = input("Enter State: ")
    if not location_state:
        print("Error: State cannot be empty.")
        return

    location_country = input("Enter Country: ")
    if not location_country:
        print("Error: Country cannot be empty.")
        return

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
    # Check if the user ID exists
    try:
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if not result:
            print("Error: User ID does not exist.")
            return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
    # Check if the user ID is empty
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
    # Check if the user ID exists
    try:
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if not result:
            print("Error: User ID does not exist.")
            return
    except Exception as e:
        print(f"An error occurred: {e}")
        return
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
            try:
                if field == "name":
                    if len(value) < 2 or len(value) > 20:
                        raise ValueError("Name must be between 2 and 20 characters")
                elif field == "dob":
                    datetime.datetime.strptime(value, '%Y-%m-%d')
                elif field == "profile_pic":
                    if not value.endswith(".jpg") and not value.endswith(".png") and not value.endswith(".jpeg"):
                        raise ValueError("Profile picture URL must end with .jpg, .png, or .jpeg")
                elif field == "age":
                    if not value.isdigit() or int(value) <= 0:
                        raise ValueError("Age must be a positive integer")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                print(f"An error occurred: {e}")
                return

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
        print("Error: User ID must be a digit")
        return

    try:
        # Check if the user ID exists
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if not result:
            print("Error: User ID does not exist.")
            return

        query = "DELETE FROM user WHERE user_id = %s"
        # Execute the delete query with the provided user ID
        cursor.execute(query, (user_id,))
        connection.commit()
        print("User deleted successfully")
    except Exception as e:
        # Rollback in case of any error during deletion
        connection.rollback()
        print(f"An error occurred: {e}")
        return
    finally:
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
