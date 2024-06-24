import os
import snowflake.connector
from textblob import TextBlob
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Establish connection
conn = snowflake.connector.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    database=os.getenv('SNOWFLAKE_DATABASE'),
    schema=os.getenv('SNOWFLAKE_SCHEMA')
)

# Function to fetch data and analyze sentiment
def fetch_and_analyze():
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT id, text FROM sentiment_analysis_data WHERE sentiment IS NULL")
        results = cursor.fetchall()
        for id, text in results:
            analysis = TextBlob(text)
            sentiment = analysis.sentiment.polarity  # Returns a polarity score between -1 and 1
            # Update the record with the sentiment score
            cursor.execute("UPDATE sentiment_analysis_data SET sentiment = %s WHERE id = %s", (sentiment, id))
    finally:
        cursor.close()

# Run the function
fetch_and_analyze()
