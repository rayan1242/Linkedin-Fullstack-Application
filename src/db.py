import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
<<<<<<< HEAD
            password="Aditya.dev31",
=======
            password="147qew147",
>>>>>>> c8ea4a8ed513e20d0556fc9223ab29b27b52b3f9
            database="linkedin"
        )
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
    
__all__ = ['connect_to_database']