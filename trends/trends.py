import os
from dotenv import load_dotenv
import snowflake.connector
import pandas as pd

# Load environment variables from .env file
load_dotenv()

# Function to establish a connection to Snowflake


def get_snowflake_connection():
    return snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        database='TREND_ANALYSIS_DB',
        schema='ANALYSIS_SCHEMA'
    )

# Function to insert sample data into the database


def insert_data():
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("""
            INSERT INTO ACTIVITY_DATA (USER_ID, ACTIVITY_COUNT, ACTIVITY_DATE) VALUES
            (101, 5, '2023-01-01'),
            (101, 7, '2023-01-02'),
            (102, 3, '2023-01-01'),
            (102, 9, '2023-01-02');
        """)
        conn.commit()  # Commit the transaction
    finally:
        cursor.close()
        conn.close()

# Function to fetch data from the database


def fetch_data():
    conn = get_snowflake_connection()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "SELECT USER_ID, ACTIVITY_COUNT, ACTIVITY_DATE FROM ACTIVITY_DATA")
        rows = cursor.fetchall()
        return pd.DataFrame(rows, columns=['User ID', 'Activity Count', 'Activity Date'])
    finally:
        cursor.close()
        conn.close()


# Example usage
if __name__ == "__main__":
    insert_data()  # Uncomment this line if you need to insert the data
    df = fetch_data()
    print(df)
