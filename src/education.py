import mysql.connector
from db import connect_to_database

connection = connect_to_database()

def create_education(education_data,connection):
    cursor = connection.cursor(dictionary=True)

    user_id = education_data.get("user_id")
    institution_id = education_data.get("institution_id")
    start_date = education_data.get("start_date")
    end_date = education_data.get("end_date")
    course = education_data.get("course")

    try:
        if not isinstance(user_id, int):
            raise ValueError("User ID must be an integer.")
        if not isinstance(institution_id, int):
            raise ValueError("Institution ID must be an integer.")
        if not isinstance(course, str) or not course:
            raise ValueError("Course must be a non-empty string.")
        datetime.datetime.strptime(start_date, '%Y-%m-%d')
        if end_date:
            datetime.datetime.strptime(end_date, '%Y-%m-%d')
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO education (user_id, institution_id, course, start_date, end_date)
                   VALUES (%s, %s, %s, %s, %s)"""
        values = (user_id, institution_id, course, start_date, end_date)

        cursor.execute(query, values)
        connection.commit()
        education_id = cursor.lastrowid

        # Retrieve the created education data
        cursor.execute("SELECT * FROM education WHERE education_id = %s", (education_id,))
        created_education = cursor.fetchone()
        return {"status": "success", "education": created_education}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_education(user_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM education WHERE user_id = %s"
        cursor.execute(query, (user_id,))
        results = cursor.fetchall()

        if results:
            return {"status": "success", "educations": results}
        else:
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

def update_education( education_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM education WHERE education_id = %s", (education_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Education ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["user_id", "institution_id", "course", "start_date", "end_date"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field in ["user_id", "institution_id"]:
                    value = int(value)
                elif field in ["start_date", "end_date"]:
                    datetime.datetime.strptime(value, '%Y-%m-%d')
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
        query = f"UPDATE education SET {', '.join(updates)} WHERE education_id = %s"
        values.append(education_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated education data
        cursor.execute("SELECT * FROM education WHERE education_id = %s", (education_id,))
        updated_education = cursor.fetchone()
        return {"status": "success", "education": updated_education}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_education( education_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM education WHERE education_id = %s", (education_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Education ID does not exist."}

        query = "DELETE FROM education WHERE education_id = %s"
        cursor.execute(query, (education_id,))
        connection.commit()
        return {"status": "success", "deleted_education_id": education_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()