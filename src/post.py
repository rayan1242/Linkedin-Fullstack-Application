import mysql.connector
from tabulate import tabulate
from db import connect_to_database
from datetime import datetime
connection = connect_to_database()

def create_post(connection):
    cursor = connection.cursor()

    user_id = input("\nEnter user ID: ")
    post_content = input("Enter post content: ")
    post_date = input("Enter post date (YYYY-MM-DD): ")
    likes = input("Enter number of likes: ")
    last_liked_at = input("Enter last liked at date (YYYY-MM-DD): ")
    # Type check and empty string check
    if not user_id.strip():
        print("User ID cannot be empty.")
        return
    if not post_content.strip():
        print("Post content cannot be empty.")
        return
    if not post_date.strip():
        print("Post date cannot be empty.")
        return

    try:
        user_id = int(user_id)
    except ValueError:
        print("User ID must be an integer.")
        return
    try:    
        likes = int(likes)
    except ValueError:
        print("Likes must be an integer.")
        return

    try:
        datetime.strptime(post_date, '%Y-%m-%d')
        if last_liked_at.strip():
            datetime.strptime(last_liked_at, '%Y-%m-%d')
    except ValueError:
        print("Date must be in YYYY-MM-DD format.")
        return
    try:
        query = """INSERT INTO post (user_id, post_content, post_date, likes, last_liked_at)
                     VALUES (%s, %s, %s, %s, %s)"""
        values = (user_id, post_content, post_date, likes, last_liked_at)
        cursor.execute(query, values)
        connection.commit()
        post_id = cursor.lastrowid
        print(f"Post created successfully with ID: {post_id}")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()
    return post_id

def read_post(connection):
    cursor = connection.cursor(dictionary=True)

    post_id = input("\nEnter post ID: ")
    if not post_id.strip():
        print("Post ID cannot be empty.")
        return
    if not post_id.isdigit():
        print("Post ID must be a number.")
        return
    try:
        query = "SELECT * FROM post WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        result = cursor.fetchone()
        if result:
            print(tabulate([result], headers="keys", tablefmt="grid"))
        else:
            print("Post not found")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def get_all_posts(connection):
    cursor = connection.cursor(dictionary=True)
    try:
        query = """
        SELECT p.post_id, u.name AS user_name, p.post_content, p.post_date, p.likes, p.last_liked_at
        FROM post p
        JOIN user u ON p.user_id = u.user_id
        """
        cursor.execute(query)
        result = cursor.fetchall()

        if result:
            # Prepare the data for tabulate
            table_data = []
            for record in result:
                table_data.append([
                    record['post_id'],
                    record['user_name'],
                    record['post_content'],
                    record['post_date'],
                    record['likes'],
                    record['last_liked_at']
                ])

            # Print the table
            print(tabulate(table_data, headers=["post_id", "user_name", "post_content", "post_date", "likes", "last_liked_at"], tablefmt="grid"))
        else:
            print("No post records found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def update_post(connection):
    cursor = connection.cursor()

    post_id = input("\nEnter post ID to update: ")
    if not post_id.strip():
        print("Post ID cannot be empty.")
        return
    if not post_id.isdigit():
        print("Post ID must be a number.")
        return
    
    fields = ["user_id", "post_content", "post_date", "likes", "last_liked_at"]
    updates = []
    values = []

    for field in fields:
        value = input(f"Enter new {field} (leave blank to skip): ")
        if value:
            if field == "user_id" or field == "likes":
                try:
                    value = int(value)
                except ValueError:
                    print(f"{field} must be an integer.")
                    return
            elif field == "post_date" or field == "last_liked_at":
                try:
                    datetime.strptime(value, '%Y-%m-%d')
                except ValueError:
                    print(f"{field} must be in YYYY-MM-DD format.")
                    return
            updates.append(f"{field} = %s")
            values.append(value)
        

    if not updates:
        print("No fields to update")
        return
    try:
        query = f"UPDATE post SET {', '.join(updates)} WHERE post_id = %s"
        values.append(post_id)
        
        cursor.execute(query, tuple(values))
        connection.commit()
        print("\nPost updated successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()

def delete_post(connection):
    cursor = connection.cursor()

    post_id = input("\nEnter post ID to delete: ")
    if not post_id.strip():
        print("Post ID cannot be empty.")
        return
    if not post_id.isdigit():
        print("Post ID must be a number.")
        return
    try:
        query = "DELETE FROM post WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        connection.commit()
        print("\nPost deleted successfully")
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        cursor.close()


def post_menu():
    connection = connect_to_database()
    
    while True:
        print("\nChoose an operation:")
        print("1: Create post")
        print("2: Read post")
        print("3. Get all post records")
        print("4: Update post")
        print("5: Delete post")
        print("0: Exit")

        choice = input("\nEnter your choice (0-4): ")

        if choice == '1':
            create_post(connection)
        elif choice == '2':
            read_post(connection)
        elif choice == '3':
            get_all_posts(connection)
        elif choice == '4':
            update_post(connection)
        elif choice == '5':
            delete_post(connection)
        elif choice == '0':
            connection.close()
            print("Database Disconnected Successfully!")
            print("\nExit from Post Menu.")
            print("\n      - X - X - X -")
            return
        else:
            print("\nInvalid choice. Please try again.")
