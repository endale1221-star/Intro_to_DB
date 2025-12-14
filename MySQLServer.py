
import mysql.connector

def create_database():
    connection = None
    try:
        # Connect to MySQL server
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password_here"
        )

        cursor = connection.cursor()

        # Create database if it does not exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except mysql.connector.Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close cursor and connection
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()
