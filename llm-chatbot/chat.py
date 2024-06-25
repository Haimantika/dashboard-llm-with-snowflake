import streamlit as st
import openai
import snowflake.connector
from snowflake.connector import DictCursor

# Initialize OpenAI with API key
openai.api_key = st.secrets["openai_api_key"]

# Function to get a Snowflake connection


def get_snowflake_connection():
    return snowflake.connector.connect(
        user=st.secrets["connections"]["snowflake"]["user"],
        password=st.secrets["connections"]["snowflake"]["password"],
        account=st.secrets["connections"]["snowflake"]["account"],
        warehouse=st.secrets["connections"]["snowflake"]["warehouse"],
        role=st.secrets["connections"]["snowflake"]["role"],
        database="TREND_ANALYSIS_DB",  # Replace with your actual database name
        schema="ANALYSIS_SCHEMA"       # Replace with your actual schema name
    )

# Function to fetch data from Snowflake


def fetch_data(query):
    with get_snowflake_connection() as conn:
        with conn.cursor(DictCursor) as cur:
            cur.execute(query)
            return cur.fetchall()

# Function to generate response using OpenAI Chat


def generate_response(user_question, data_context):
    # Convert data to a readable context for the AI model
    context = " ".join(
        [f"{row['column_name']}: {row['value']}" for row in data_context])
    prompt = f"{context}\nQuestion: {user_question}\nAnswer:"

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": prompt}
            ]
        )
        return response['choices'][0]['message']['content']
    except Exception as e:
        return str(e)


# Streamlit user interface
st.title("👻 Casper - Real Estate Data Assistant")
user_question = st.text_input("Ask a question about real estate:")

if user_question:
    # Fetch relevant data from Snowflake
    # Adjust query as needed
    data_context = fetch_data("SELECT * FROM ACTIVITY_DATA LIMIT 100")

    # Generate and display response based on the data context
    response = generate_response(user_question, data_context)
    st.write("Casper's Response:")
    st.write(response)
