from datetime import datetime
import mysql.connector
from db import connect_to_database

connection = connect_to_database()

def create_post(post_data,connection):
    cursor = connection.cursor(dictionary=True)

    user_id = post_data.get("user_id")
    post_content = post_data.get("post_content")
    post_date = post_data.get("post_date")
    last_liked_at = post_data.get("last_liked_at")
    likes = post_data.get("likes")

    try:
        # if not isinstance(user_id, int):
        #     raise ValueError("User ID must be an integer.")
        if not isinstance(post_content, str) or not post_content:
            raise ValueError("post_content must be a non-empty string.")
        datetime.strptime(post_date, '%Y-%m-%d %H:%M:%S')
        datetime.strptime(last_liked_at, '%Y-%m-%d %H:%M:%S')
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO post (user_id, post_content, post_date, last_liked_at, likes)
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (user_id, post_content, post_date, last_liked_at, likes)

        cursor.execute(query, values)
        connection.commit()
        post_id = cursor.lastrowid

        # Retrieve the created post data
        cursor.execute("SELECT * FROM post WHERE post_id = %s", (post_id,))
        created_post = cursor.fetchone()
        return {"status": "success", "post": created_post}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_post(post_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM post WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        result = cursor.fetchone()

        if result:
            return {"status": "success", "post": result}
        else:
            return {"status": "error", "message": "Post not found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_all_posts(connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM post"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            return {"status": "success", "posts": results}
        else:
            return {"status": "error", "message": "No posts found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def update_post(post_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM post WHERE post_id = %s", (post_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Post ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["user_id", "post_content", "post_date", "last_liked_at", "likes"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field == "user_id":
                    value = int(value)
                elif field == "post_date":
                    datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                elif field == "last_liked_at":
                    datetime.strptime(value, '%Y-%m-%d %H:%M:%S')
                elif field == "post_content":
                    if not isinstance(value, str):
                        raise ValueError(f"{field} must be a string.")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        query = f"UPDATE post SET {', '.join(updates)} WHERE post_id = %s"
        values.append(post_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated post data
        cursor.execute("SELECT * FROM post WHERE post_id = %s", (post_id,))
        updated_post = cursor.fetchone()
        return {"status": "success", "post": updated_post}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_post(post_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM post WHERE post_id = %s", (post_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Post ID does not exist."}

        query = "DELETE FROM post WHERE post_id = %s"
        cursor.execute(query, (post_id,))
        connection.commit()
        return {"status": "success", "deleted_post_id": post_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()