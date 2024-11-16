from tabulate import tabulate
import datetime
from db import connect_to_database

def create_user(user_data,connection):
    cursor = connection.cursor(dictionary=True)
    
    name = user_data.get("name")
    dob = user_data.get("dob")
    profile_pic = user_data.get("profile_pic")
    location_city = user_data.get("location_city")
    location_state = user_data.get("location_state")
    location_country = user_data.get("location_country")

    try:
        if len(name) < 2 or len(name) > 20:
            raise ValueError("Name must be between 2 and 20 characters")
        datetime.datetime.strptime(dob, '%Y-%m-%d')
        if not profile_pic.endswith(".jpg") and not profile_pic.endswith(".png") and not profile_pic.endswith(".jpeg"):
            raise ValueError("Profile picture URL must end with .jpg, .png, or .jpeg")
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO user (name, dob, profile_pic, location_city, location_state, location_country)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (name, dob, profile_pic, location_city, location_state, location_country)

        cursor.execute(query, values)
        connection.commit()

        user_id = cursor.lastrowid

        # Retrieve the created user data
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        created_user = cursor.fetchone()
        return {"status": "success", "user": created_user}
    except Exception as e:
        connection.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()

def get_user(user_id,connection):
    cursor = connection.cursor(dictionary=True)

    # Check if the user ID is empty
    if user_id == "":
        return {"status": "error", "message": "User ID cannot be empty."}

    try:
        # Check if the user ID exists
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "User ID does not exist."}
        
        # Return the user data
        return {"status": "success", "user": result}
    except Exception as e:
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()


def get_all_users(connection):
    cursor = connection.cursor(dictionary=True)

    # Define the SQL query to select all users from the 'user' table
    query = "SELECT * FROM user"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        users = []

        # Iterate through each user in the result set
        for user in result:
            # Append user details to the users list
            users.append({
                "user_id": user['user_id'],
                "name": user['name'],
                "dob": user['dob'],
                "age": user['age'],
                "profile_pic": user['profile_pic'],
                "location_city": user['location_city'],
                "location_state": user['location_state'],
                "location_country": user['location_country']
            })

        # Return the user data
        return {"status": "success", "users": users}
    else:
        return {"status": "error", "message": "No users found"}

    cursor.close()

def update_user(user_id, user_data,connection):
    cursor = connection.cursor(dictionary=True)

    # Check if the user ID exists
    try:
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "User ID does not exist."}
    except Exception as e:
        return {"status": "error", "message": str(e)}

    fields = ["name", "dob", "profile_pic", "location_city", "location_state", "location_country"]
    updates = []
    values = []

    # Validate and update fields
    for field in fields:
        if field in user_data:
            value = user_data[field]
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
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        # Construct the SQL update query
        query = f"UPDATE user SET {', '.join(updates)} WHERE user_id = %s"
        values.append(user_id)

        # Execute the update query
        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated user data
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        updated_user = cursor.fetchone()
        return {"status": "success", "user": updated_user}
    except Exception as e:
        connection.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()

def delete_user(user_id,connection,):
    cursor = connection.cursor(dictionary=True)
    
    # Check if the user ID is empty
    if user_id == "":
        return {"status": "error", "message": "User ID cannot be empty."}
    if not isinstance(user_id, int):
        return {"status": "error", "message": "User ID must be an integer"}

    try:
        # Check if the user ID exists
        cursor.execute("SELECT * FROM user WHERE user_id = %s", (user_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "User ID does not exist."}

        query = "DELETE FROM user WHERE user_id = %s"
        # Execute the delete query with the provided user ID
        cursor.execute(query, (user_id,))
        connection.commit()
        return {"status": "success", "deleted_user_id": user_id}
    except Exception as e:
        # Rollback in case of any error during deletion
        connection.rollback()
        return {"status": "error", "message": str(e)}
    finally:
        cursor.close()

