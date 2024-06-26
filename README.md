# Real Estate Price Prediction Dashboard

## Project Overview

This project develops a dashboard that fetches historical real estate price data from Snowflake, and visualizes these predictions in a Streamlit web application. The system is engineered to pull historical data from Snowflake, and provide an chat assistant for users to query future real estate prices using NLP.

## Architecture

- **Snowflake**: Acts as the primary data warehouse, storing historical real estate data.
- **Python**: Utilized as the main programming language, interfacing with Snowflake to retrieve data and using `scikit-learn` for building the predictive model.
- **scikit-learn**: A Python library for machine learning, used here to train a linear regression model for price prediction.
- **Streamlit**: Used to build and deploy the interactive web dashboard that visualizes data and predictions.
- **.env File**: Manages sensitive credentials for Snowflake securely.

## Setup Instructions

1. **Environment Setup**:
   - Ensure Python is installed on your system.
   - Install required Python packages:
     ```bash
     pip install snowflake-connector-python streamlit scikit-learn python-dotenv pandas
     ```

2. **Configure Environment Variables**:
   - Create a `.env` file in your project root with the following keys:
     ```
     SNOWFLAKE_USER=your_username
     SNOWFLAKE_PASSWORD=your_password
     SNOWFLAKE_ACCOUNT=your_account_id
     SNOWFLAKE_WAREHOUSE=your_warehouse
     SNOWFLAKE_ROLE=your_role
     SNOWFLAKE_DATABASE=your_database
     SNOWFLAKE_SCHEMA=your_schema
     ```

3. For the chat assistant, have a secrets.toml file with the following keys:
   ```
   openai_api_key = "your key"
   [connections.snowflake]
   user = "your username"
   password = "your password"
   warehouse = "your warehouse"
   role = "your role"
   account = "your account"
   ```

3. **Database Setup**:
   - Log into your Snowflake account and ensure the `REAL_ESTATE_DATA` table is set up with the correct schema.

4. **Running the dashboard file**:
   - Launch the streamlit dashboard to see the price analysis
     ```bash
     streamlit run stm.py
     ```

5. **Running the chatbot**:
   - Launch the Streamlit dashboard to interact with the assistant:
     ```bash
     streamlit run chat.py
     ```

## Resources

- [Snowflake Documentation](https://docs.snowflake.com)
- [Streamlit Documentation](https://docs.streamlit.io)
- [scikit-learn Documentation](https://scikit-learn.org/stable/)
- [Python `.env` Usage](https://pypi.org/project/python-dotenv/)

## Troubleshooting

- Ensure all environment variables are correctly set in the `.env` file.
- Check network settings if there is difficulty connecting to Snowflake.
- Verify that all Python packages are installed and up to date.




