# streamlit_app.py

import streamlit as st
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
import os

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

# Function to fetch data
def get_data():
    sql_query = "SELECT id, text, sentiment FROM sentiment_analysis_data"
    df = pd.read_sql(sql_query, conn)
    return df

# Streamlit app
st.title('Sentiment Analysis Dashboard')
df = get_data()
st.write(df)

# Optionally, add more interactive components
if st.button('Refresh Data'):
    df = get_data()
    st.write(df)
