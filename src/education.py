import mysql.connector
from db import connect_to_database
from datetime import datetime
connection = connect_to_database()

def create_education(education_data,connection):
    cursor = connection.cursor(dictionary=True)

    user_id = education_data.get("user_id")
    institution_id = education_data.get("institution_id")
    start = education_data.get("start")
    end = education_data.get("end")
    course = education_data.get("course")

    try:
        # if not isinstance(user_id, int):
        #     raise ValueError("User ID must be an integer.")
        if not isinstance(institution_id, int):
            raise ValueError("Institution ID must be an integer.")
        if not isinstance(course, str) or not course:
            raise ValueError("Course must be a non-empty string.")
        if start:
            start = datetime.strptime(start, '%Y-%m-%d').date()
        else:
            raise ValueError("Start date must be provided and in 'YYYY-MM-DD' format.")
        if end:
            end = datetime.strptime(end, '%Y-%m-%d').date()
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO education (user_id, institution_id, course, start, end)
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (user_id, institution_id, course, start, end)

        cursor.execute(query, values)
        connection.commit()
        education_id = cursor.lastrowid

        # Retrieve the created education data
        cursor.execute("SELECT * FROM education WHERE edu_id = %s", (education_id,))
        created_education = cursor.fetchone()
        return {"status": "success", "education": created_education}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_education(user_id,connection):
    cursor = connection.cursor(dictionary=True)
    user_id = int(user_id)

    try:
        query = "SELECT * FROM education WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()
        if results:
            for result in results:
                result.pop("start", None)
                result.pop("end", None)
                print(results)   
            return {"status": "success", "educations": results}
        return {"status": "error", "message": "No education records found for this user."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_all_educations(connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM education"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            return {"status": "success", "educations": results}
        else:
            return {"status": "error", "message": "No education records found."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def update_education( edu_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM education WHERE edu_id = %s", (edu_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Education ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["user_id", "institution_id", "course", "start", "end"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field in ["user_id", "institution_id"]:
                    value = int(value)
                elif field in ["start", "end"]:
                    datetime.strptime(value, '%Y-%m-%d')
                elif field == "course":
                    if not isinstance(value, str):
                        raise ValueError(f"{field} must be a string.")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        query = f"UPDATE education SET {', '.join(updates)} WHERE edu_id = %s"
        values.append(edu_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated education data
        cursor.execute("SELECT * FROM education WHERE edu_id = %s", (edu_id,))
        updated_education = cursor.fetchone()
        return {"status": "success", "education": updated_education}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_education( edu_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        edu = int(edu_id)
        cursor.execute("SELECT * FROM education WHERE edu_id = %s", (edu_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Education ID does not exist."}

        query = "DELETE FROM education WHERE edu_id = %s"
        cursor.execute(query, (edu_id,))
        connection.commit()
        return {"status": "success", "deleted_education_id": edu_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()