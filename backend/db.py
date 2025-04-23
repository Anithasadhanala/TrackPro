import os
from dotenv import load_dotenv
import mysql.connector
from mysql.connector import Error


# Load environment variables from .env
load_dotenv()

def get_db_connection():
    try:
        # Actual database credentials
        connection = mysql.connector.connect(
            host=os.getenv("DB_HOST"),
            port=(os.getenv("DB_PORT")),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            database=os.getenv("DB_NAME")
        )
        
        if connection.is_connected():
            print("Connected to MySQL database")
            return connection
        else:
            print("Failed to connect to MySQL database")
            return None
    except Error as e:
        print(f"Error: {e}")
        return None

# Main code to use the connection
connection = get_db_connection() 


# Check if the connection was successfully established
if connection:  
    cursor = connection.cursor()
    cursor.execute("SELECT 1") 
    result = cursor.fetchone()
    
    if result:
        print("Database connection is verified by executing a query")
    
    cursor.close() 
    connection.close()  
else:
    print("Connection failed.")
