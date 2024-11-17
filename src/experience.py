import mysql.connector
from db import connect_to_database
from datetime import datetime

connection = connect_to_database()

def create_experience(experience_data,connection):
    cursor = connection.cursor(dictionary=True)

    user_id = experience_data.get("user_id")
    title = experience_data.get("title")
    company = experience_data.get("company")
    start_date = experience_data.get("start_date")
    end_date = experience_data.get("end_date")
    description = experience_data.get("description")

    try:
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if not isinstance(title, str) or not title:
            raise ValueError("Title must be a non-empty string.")
        if not isinstance(company, str) or not company:
            raise ValueError("Company must be a non-empty string.")
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        if end_date:
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO experience (user_id, title, company, start_date, end_date, description)
                   VALUES (%s, %s, %s, %s, %s, %s)"""
        values = (user_id, title, company, start_date, end_date, description)

        cursor.execute(query, values)
        connection.commit()
        exp_id = cursor.lastrowid

        # Retrieve the created experience data
        cursor.execute("SELECT * FROM experience WHERE experience_id = %s", (exp_id,))
        created_experience = cursor.fetchone()
        return {"status": "success", "experience": created_experience}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_experience(user_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM experience WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()

        if results:
            return {"status": "success", "experiences": results}
        else:
            return {"status": "error", "message": "No experiences found for this user."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_all_experiences(connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM experience"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            return {"status": "success", "experiences": results}
        else:
            return {"status": "error", "message": "No experiences found."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def update_experience(exp_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM experience WHERE experience_id = %s", (exp_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Experience ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["title", "company", "start_date", "end_date", "description"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field == "title":
                    if not isinstance(value, str) or not value:
                        raise ValueError("Title must be a non-empty string.")
                elif field == "company":
                    if not isinstance(value, str) or not value:
                        raise ValueError("Company must be a non-empty string.")
                elif field in ["start_date", "end_date"]:
                    datetime.datetime.strptime(value, '%Y-%m-%d')
                elif field == "description":
                    if not isinstance(value, str):
                        raise ValueError("Description must be a string.")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        query = f"UPDATE experience SET {', '.join(updates)} WHERE experience_id = %s"
        values.append(exp_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated experience data
        cursor.execute("SELECT * FROM experience WHERE experience_id = %s", (exp_id,))
        updated_experience = cursor.fetchone()
        return {"status": "success", "experience": updated_experience}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_experience( exp_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM experience WHERE experience_id = %s", (exp_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Experience ID does not exist."}

        query = "DELETE FROM experience WHERE experience_id = %s"
        cursor.execute(query, (exp_id,))
        connection.commit()
        return {"status": "success", "deleted_experience_id": exp_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()