try:
    import mysql.connector
    from mysql.connector import Error
except ImportError as e:
    raise ImportError("mysql.connector not found. Install with: pip install mysql-connector-python") from e


def create_database():
    connection = None
    cursor = None
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="my_password"
        )

        cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

        print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        if connection is not None and getattr(connection, "is_connected", lambda: False)():
            if cursor:
                cursor.close()
            connection.close()

if __name__ == "__main__":
    create_database()