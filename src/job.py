import mysql.connector
from db import connect_to_database

connection = connect_to_database()

def create_job(job_data,connection):
    cursor = connection.cursor(dictionary=True)

    institution_id = job_data.get("institution_id")
    job_title = job_data.get("job_title")
    description = job_data.get("description")
    type = job_data.get("type")

    try:
        if not isinstance(institution_id, int):
            raise ValueError("Institution ID must be an integer.")
        if not isinstance(job_title, str) or not job_title:
            raise ValueError("Job title must be a non-empty string.")
        if not isinstance(description, str) or not description:
            raise ValueError("Description must be a non-empty string.")
        if not isinstance(type, str) or not type:
            raise ValueError("Job type must be a non-empty string.")
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO job (institution_id, job_title, description, type)
                   VALUES (%s, %s, %s, %s)"""
        values = (institution_id, job_title, description, type)

        cursor.execute(query, values)
        connection.commit()
        job_id = cursor.lastrowid

        # Retrieve the created job data
        cursor.execute("SELECT * FROM job WHERE job_id = %s", (job_id,))
        created_job = cursor.fetchone()
        return {"status": "success", "job": created_job}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_job(job_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM job WHERE job_id = %s"
        cursor.execute(query, (job_id,))
        result = cursor.fetchone()

        if result:
            return {"status": "success", "job": result}
        else:
            return {"status": "error", "message": "Job not found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_all_jobs(connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM job"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            return {"status": "success", "jobs": results}
        else:
            return {"status": "error", "message": "No jobs found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def update_job( job_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM job WHERE job_id = %s", (job_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Job ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["institution_id", "job_title", "description", "type"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field == "institution_id":
                    value = int(value)
                elif field in ["job_title", "description", "type"]:
                    if not isinstance(value, str):
                        raise ValueError(f"{field} must be a string.")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        query = f"UPDATE job SET {', '.join(updates)} WHERE job_id = %s"
        values.append(job_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated job data
        cursor.execute("SELECT * FROM job WHERE job_id = %s", (job_id,))
        updated_job = cursor.fetchone()
        return {"status": "success", "job": updated_job}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_job( job_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM job WHERE job_id = %s", (job_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Job ID does not exist."}

        query = "DELETE FROM job WHERE job_id = %s"
        cursor.execute(query, (job_id,))
        connection.commit()
        return {"status": "success", "deleted_job_id": job_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()