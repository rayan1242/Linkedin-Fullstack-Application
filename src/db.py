import mysql.connector

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="127.0.0.1",
            user="root",
            password="root",
            database="linkedin"
        )
        print("\nConnected to the database successfully!!")
        return connection
    except mysql.connector.Error as err:
        print(f"Error connecting to the database: {err}")
        return None
