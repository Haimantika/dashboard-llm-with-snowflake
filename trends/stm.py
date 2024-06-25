import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import snowflake.connector
from dotenv import load_dotenv
import os

# Load environment variables from .env
load_dotenv()

# Establish a connection to Snowflake


def get_snowflake_connection():
    return snowflake.connector.connect(
        user=os.getenv('SNOWFLAKE_USER'),
        password=os.getenv('SNOWFLAKE_PASSWORD'),
        account=os.getenv('SNOWFLAKE_ACCOUNT'),
        database='TREND_ANALYSIS_DB',
        schema='ANALYSIS_SCHEMA'
    )

# Fetch real estate data from Snowflake


def fetch_data():
    conn = get_snowflake_connection()
    query = "SELECT YEAR, AVERAGE_PRICE FROM REAL_ESTATE_DATA ORDER BY YEAR"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# Initialize Streamlit app
st.title('Real Estate Price Trend Dashboard')

# Load data
df = fetch_data()

# Convert YEAR to datetime for better plotting
df['YEAR'] = pd.to_datetime(df['YEAR'], format='%Y')

# Display data as a table
st.write("### Data Overview", df)

# Line chart for average price trends
st.write("### Average Price Trend Over Years")
st.line_chart(df.set_index('YEAR')['AVERAGE_PRICE'])

# Bar chart for average price comparison
st.write("### Yearly Average Price Comparison")
fig, ax = plt.subplots()
ax.bar(df['YEAR'].dt.strftime('%Y'), df['AVERAGE_PRICE'], color='skyblue')
plt.xticks(rotation=45, ha='right')
plt.xlabel('Year')
plt.ylabel('Average Price ($)')
st.pyplot(fig)


if st.button('Refresh Data'):
    st.experimental_rerun()
