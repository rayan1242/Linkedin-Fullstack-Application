import mysql.connector
from db import connect_to_database
from datetime import datetime
connection = connect_to_database()

def create_application(application_data,connection):
    cursor = connection.cursor(dictionary=True)

    user_id = application_data.get("user_id")
    job_id = application_data.get("job_id")
    status = application_data.get("status")
    applied_date = application_data.get("applied_date")

    try:
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if not isinstance(job_id, int):
            raise ValueError("Job ID must be an integer.")
        if not isinstance(status, str) or not status:
            raise ValueError("Status must be a non-empty string.")
        datetime.datetime.strptime(applied_date, '%Y-%m-%d')
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO application (user_id, job_id, status, applied_date)
                   VALUES (%s, %s, %s, %s)"""
        values = (user_id, job_id, status, applied_date)

        cursor.execute(query, values)
        connection.commit()
        application_id = cursor.lastrowid

        # Retrieve the created application data
        cursor.execute("SELECT * FROM application WHERE application_id = %s", (application_id,))
        created_application = cursor.fetchone()
        return {"status": "success", "application": created_application}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_application(application_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM application WHERE application_id = %s"
        cursor.execute(query, (application_id,))
        result = cursor.fetchone()

        if result:
            return {"status": "success", "application": result}
        else:
            return {"status": "error", "message": "Application not found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_all_applications(connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM application"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            return {"status": "success", "applications": results}
        else:
            return {"status": "error", "message": "No applications found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def update_application(application_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM application WHERE application_id = %s", (application_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Application ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["user_id", "job_id", "status", "applied_date"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field in ["user_id", "job_id"]:
                    value = int(value)
                elif field == "applied_date":
                    datetime.datetime.strptime(value, '%Y-%m-%d')
                elif field == "status":
                    if not isinstance(value, str):
                        raise ValueError(f"{field} must be a string.")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        query = f"UPDATE application SET {', '.join(updates)} WHERE application_id = %s"
        values.append(application_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated application data
        cursor.execute("SELECT * FROM application WHERE application_id = %s", (application_id,))
        updated_application = cursor.fetchone()
        return {"status": "success", "application": updated_application}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_application(application_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM application WHERE application_id = %s", (application_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Application ID does not exist."}

        query = "DELETE FROM application WHERE application_id = %s"
        cursor.execute(query, (application_id,))
        connection.commit()
        return {"status": "success", "deleted_application_id": application_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()