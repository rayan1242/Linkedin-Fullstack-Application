import mysql.connector
from db import connect_to_database

connection = connect_to_database()

def create_skill(skill_data,connection):
    cursor = connection.cursor(dictionary=True)
    
    skill_name = skill_data.get("skill_name")
    
    if not skill_name:
        return {"status": "error", "message": "Skill name cannot be empty."}
    
    try:
        query = "INSERT INTO skill (skill_name) VALUES (%s)"
        values = (skill_name,)
        cursor.execute(query, values)
        connection.commit()

        skill_id = cursor.lastrowid

        # Retrieve the created skill data
        cursor.execute("SELECT * FROM skill WHERE skill_id = %s", (skill_id,))
        created_skill = cursor.fetchone()
        return {"status": "success", "skill": created_skill}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_skill(skill_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM skill WHERE skill_id = %s"
        cursor.execute(query, (skill_id,))
        result = cursor.fetchone()

        if result:
            return {"status": "success", "skill": result}
        else:
            return {"status": "error", "message": "Skill not found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_all_skills(connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM skill"
        cursor.execute(query)
        results = cursor.fetchall()

        if results:
            return {"status": "success", "skills": results}
        else:
            return {"status": "error", "message": "No skills found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def update_skill(skill_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM skill WHERE skill_id = %s", (skill_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Skill ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["skill_name"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field == "skill_name":
                    if not isinstance(value, str) or not value:
                        raise ValueError("Skill name must be a non-empty string.")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        query = f"UPDATE skill SET {', '.join(updates)} WHERE skill_id = %s"
        values.append(skill_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated skill data
        cursor.execute("SELECT * FROM skill WHERE skill_id = %s", (skill_id,))
        updated_skill = cursor.fetchone()
        return {"status": "success", "skill": updated_skill}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_skill(skill_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM skill WHERE skill_id = %s", (skill_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Skill ID does not exist."}

        query = "DELETE FROM skill WHERE skill_id = %s"
        cursor.execute(query, (skill_id,))
        connection.commit()
        return {"status": "success", "deleted_skill_id": skill_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()