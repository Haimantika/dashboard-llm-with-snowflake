# Sentiment Analysis Dashboard

## Project Overview

This project implements a sentiment analysis dashboard that pulls textual data from Snowflake, analyzes sentiment using the TextBlob library, and visualizes the results in a Streamlit web application. The system is designed to process unanalyzed text stored in Snowflake, update the database with sentiment scores, and provide an interactive interface for users to view and refresh sentiment analysis results.

## Architecture

- **Snowflake**: Used as the central data storage and management system. It stores all the text data and sentiment scores.
- **Python**: Serves as the backend processing language, using Snowflake connectors to interact with the database and TextBlob for sentiment analysis.
- **TextBlob**: A Python library used for processing textual data and providing sentiment analysis.
- **Streamlit**: A Python framework for creating and sharing beautiful, custom web apps for machine learning and data science.
- **.env File**: Contains sensitive information such as Snowflake credentials and is used to securely manage environment variables.

## Project Directory Structure
```
/dashboard-llm-with-snwoflake
│
├── .env # Environment variables file
├── sentiment_analysis.py # Script for performing sentiment analysis and updating Snowflake
├── streamlit_app.py # Streamlit application for displaying the sentiment analysis results
└── README.md # Documentation for the project
```


## Setup Instructions

1. **Environment Setup**:
   - Ensure Python is installed on your system.
   - Install required Python packages:
     ```bash
     pip install snowflake-connector-python streamlit textblob python-dotenv pandas
     ```

2. **Configure Environment Variables**:
   - Create a `.env` file in your project root with the following keys:
     ```
     SNOWFLAKE_USER=your_username
     SNOWFLAKE_PASSWORD=your_password
     SNOWFLAKE_ACCOUNT=your_account_id
     SNOWFLAKE_DATABASE=your_database
     SNOWFLAKE_SCHEMA=your_schema
     ```

3. **Database Setup**:
   - Log into your Snowflake account and ensure the `SENTIMENT_ANALYSIS_DATA` table is created as per the provided SQL schema.

4. **Running the Sentiment Analysis Script**:
   - Execute the sentiment analysis script to analyze and update sentiment scores:
     ```bash
     python sentiment_analysis.py
     ```

5. **Running the Streamlit Application**:
   - Launch the Streamlit dashboard to view the analysis results:
     ```bash
     streamlit run streamlit_app.py
     ```

## Resources

- [Snowflake Documentation](https://docs.snowflake.com)
- [Streamlit Documentation](https://docs.streamlit.io)
- [TextBlob Documentation](https://textblob.readthedocs.io/en/dev/)
- [Python `.env` Usage](https://pypi.org/project/python-dotenv/)

## Troubleshooting

- Ensure all environment variables are correctly set in the `.env` file.
- Check network settings if there is difficulty connecting to Snowflake.
- Verify that the Python packages are installed and up to date.


