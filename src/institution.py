import mysql.connector
from db import connect_to_database

connection = connect_to_database()

def create_institution(institution_data,connection):
    cursor = connection.cursor(dictionary=True)

    no_of_employees = institution_data.get("no_of_employees")
    website = institution_data.get("website")
    industry = institution_data.get("industry")
    name = institution_data.get("name")
    description = institution_data.get("description")
    location_city = institution_data.get("location_city")
    location_state = institution_data.get("location_state")
    location_country = institution_data.get("location_country")

    try:
        no_of_employees = int(no_of_employees)
        if not isinstance(website, str) or not (website.startswith("http://") or website.startswith("https://")):
            raise ValueError("Website must be a string and start with 'http://' or 'https://'.")
        if not isinstance(industry, str):
            raise ValueError("Industry must be a string.")
        if not isinstance(name, str) or not name:
            raise ValueError("Name must be a non-empty string.")
        if not isinstance(description, str):
            raise ValueError("Description must be a string.")
        if not isinstance(location_city, str) or not location_city:
            raise ValueError("City must be a non-empty string.")
        if not isinstance(location_state, str) or not location_state:
            raise ValueError("State must be a non-empty string.")
        if not isinstance(location_country, str) or not location_country:
            raise ValueError("Country must be a non-empty string.")
    except ValueError as e:
        return {"status": "error", "message": str(e)}

    try:
        query = """INSERT INTO institution (no_of_employees, website, industry, name, description, 
                   location_city, location_state, location_country) 
                   VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (no_of_employees, website, industry, name, description, 
                  location_city, location_state, location_country)

        cursor.execute(query, values)
        connection.commit()
        institution_id = cursor.lastrowid

        # Retrieve the created institution data
        cursor.execute("SELECT * FROM institution WHERE institution_id = %s", (institution_id,))
        created_institution = cursor.fetchone()
        return {"status": "success", "institution": created_institution}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_institution(institution_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        query = "SELECT * FROM institution WHERE institution_id = %s"
        cursor.execute(query, (institution_id,))
        result = cursor.fetchone()
        
        if result:
            return {"status": "success", "institution": result}
        else:
            return {"status": "error", "message": "Institution not found"}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def get_all_institutions(connection):
    cursor = connection.cursor(dictionary=True)

    query = "SELECT * FROM institution"
    cursor.execute(query)
    result = cursor.fetchall()

    if result:
        institutions = []
        for record in result:
            institutions.append({
                "institution_id": record['institution_id'],
                "name": record['name'],
                "no_of_employees": record['no_of_employees'],
                "website": record['website'],
                "industry": record['industry'],
                "description": record['description'],
                "location_city": record['location_city'],
                "location_state": record['location_state'],
                "location_country": record['location_country']
            })
        return {"status": "success", "institutions": institutions}
    else:
        return {"status": "error", "message": "No institution records found"}

    cursor.close()

def update_institution(institution_id, update_data,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM institution WHERE institution_id = %s", (institution_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Institution ID does not exist."}
    except mysql.connector.Error as err:
        return {"status": "error", "message": str(err)}

    fields = ["no_of_employees", "website", "industry", "name", "description", 
              "location_city", "location_state", "location_country"]
    updates = []
    values = []

    for field in fields:
        if field in update_data:
            value = update_data[field]
            try:
                if field == "no_of_employees":
                    value = int(value)
                elif field == "website":
                    if not (value.startswith("http://") or value.startswith("https://")):
                        raise ValueError("Website must start with 'http://' or 'https://'.")
                elif field in ["industry", "name", "description", "location_city", "location_state", "location_country"]:
                    if not isinstance(value, str):
                        raise ValueError(f"{field} must be a string.")
                updates.append(f"{field} = %s")
                values.append(value)
            except ValueError as e:
                return {"status": "error", "message": str(e)}

    if not updates:
        return {"status": "error", "message": "No fields to update"}

    try:
        query = f"UPDATE institution SET {', '.join(updates)} WHERE institution_id = %s"
        values.append(institution_id)

        cursor.execute(query, tuple(values))
        connection.commit()

        # Retrieve the updated institution data
        cursor.execute("SELECT * FROM institution WHERE institution_id = %s", (institution_id,))
        updated_institution = cursor.fetchone()
        return {"status": "success", "institution": updated_institution}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()

def delete_institution(institution_id,connection):
    cursor = connection.cursor(dictionary=True)

    try:
        cursor.execute("SELECT * FROM institution WHERE institution_id = %s", (institution_id,))
        result = cursor.fetchone()
        if not result:
            return {"status": "error", "message": "Institution ID does not exist."}

        query = "DELETE FROM institution WHERE institution_id = %s"
        cursor.execute(query, (institution_id,))
        connection.commit()
        return {"status": "success", "deleted_institution_id": institution_id}
    except mysql.connector.Error as err:
        connection.rollback()
        return {"status": "error", "message": str(err)}
    finally:
        cursor.close()