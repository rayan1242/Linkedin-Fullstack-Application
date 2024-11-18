import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="147qwe147",
            database="linkedin"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
    
__all__ = ['connect_to_database']