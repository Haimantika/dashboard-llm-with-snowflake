import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from dotenv import load_dotenv
import os
import snowflake.connector

# Load environment variables from .env
load_dotenv()

# Establish connection to Snowflake


def get_snowflake_connection():
    return snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        database='TREND_ANALYSIS_DB',
        schema='ANALYSIS_SCHEMA'
    )

# Fetch data from Snowflake


def fetch_data():
    conn = get_snowflake_connection()
    query = "SELECT ACTIVITY_DATE, SUM(ACTIVITY_COUNT) AS TOTAL_ACTIVITY FROM ACTIVITY_DATA GROUP BY ACTIVITY_DATE ORDER BY ACTIVITY_DATE"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# Initialize Streamlit app
st.title('Activity Trend Analysis Dashboard')

# Load data
df = fetch_data()
df['ACTIVITY_DATE'] = pd.to_datetime(df['ACTIVITY_DATE'])

# Display data as a table
st.write("### Data Overview", df)

# Line chart for activity trends
st.write("### Activity Trend Over Time")
st.line_chart(df.set_index('ACTIVITY_DATE')['TOTAL_ACTIVITY'])

# Bar chart for activity comparison
st.write("### Daily Activity Comparison")
fig, ax = plt.subplots()
ax.bar(df['ACTIVITY_DATE'].dt.strftime('%Y-%m-%d'),
       df['TOTAL_ACTIVITY'], color='blue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Date')
plt.ylabel('Total Activity')
st.pyplot(fig)

# Optional: Refresh Data Button
if st.button('Refresh Data'):
    st.experimental_rerun()
