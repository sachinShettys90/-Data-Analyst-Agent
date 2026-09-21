from agno.tools.pandas import PandasTools
from agno.tools.duckdb import DuckDbTools
from agno.models.openai import OpenAIChat
from agno.agent import Agent
import tempfile
import csv
import os
import streamlit as st
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Function to preprocess and save the uploaded file


def preprocess_and_save(file):
    try:
        # Read the uploaded file into a DataFrame
        if file.name.endswith('.csv'):
            df = pd.read_csv(file, encoding='utf-8',
                             na_values=['NA', 'N/A', 'missing'])
        elif file.name.endswith('.xlsx'):
            df = pd.read_excel(file, na_values=['NA', 'N/A', 'missing'])
        else:
            st.error("Unsupported file format. Please upload a CSV or Excel file.")
            return None, None, None

        # Parse dates and numeric columns
        for col in df.columns:
            if 'date' in col.lower():
                df[col] = pd.to_datetime(df[col], errors='coerce')
            elif df[col].dtype == 'object':
                try:
                    df[col] = pd.to_numeric(df[col])
                except (ValueError, TypeError):
                    # Keep as is if conversion fails
                    pass

        # Create a temporary file to save the preprocessed data
        with tempfile.NamedTemporaryFile(delete=False, suffix=".csv") as temp_file:
            temp_path = temp_file.name
            # Save the DataFrame to the temporary CSV file with quotes around string fields
            df.to_csv(temp_path, index=False, quoting=csv.QUOTE_ALL)

        return temp_path, df.columns.tolist(), df  # Return the DataFrame as well
    except Exception as e:
        st.error(f"Error processing file: {e}")
        return None, None, None


# Streamlit app
st.title("📊 Data Analyst Agent")

# Stop early with a clear message if the key isn't configured, instead of
# letting the agent fail later with a less obvious error.
if not OPENAI_API_KEY:
    st.error(
        "OPENAI_API_KEY not found. Add it to a `.env` file in the project "
        "root, e.g.:\n\nOPENAI_API_KEY=sk-..."
    )
    st.stop()

# File upload widget
uploaded_file = st.file_uploader(
    "Upload a CSV or Excel file", type=["csv", "xlsx"])

if uploaded_file is not None:
    # Preprocess and save the uploaded file
    temp_path, columns, df = preprocess_and_save(uploaded_file)

    if temp_path and columns and df is not None:
        # Display the uploaded data as a table
        st.write("Uploaded Data:")
        st.dataframe(df)  # Use st.dataframe for an interactive table

        # Display the columns of the uploaded data
        st.write("Uploaded columns:", columns)

        # Initialize DuckDbTools
        duckdb_tools = DuckDbTools()

        # Load the CSV file into DuckDB as a table
        duckdb_tools.load_local_csv_to_table(
            path=temp_path,
            table="uploaded_data",
        )

        # Initialize the Agent with DuckDB and Pandas tools
        data_analyst_agent = Agent(
            model=OpenAIChat(id="gpt-4o", api_key=OPENAI_API_KEY),
            tools=[duckdb_tools, PandasTools()],
            system_message="You are an expert data analyst. Use the 'uploaded_data' table to answer user queries. Generate SQL queries using DuckDB tools to solve the user's query. Provide clear and concise answers with the results.",
            markdown=True,
        )

        # Initialize code storage in session state
        if "generated_code" not in st.session_state:
            st.session_state.generated_code = None

        # Main query input widget
        user_query = st.text_area("Ask a query about the data:")

        # Add info message about terminal output
        st.info("💡 Check your terminal for a clearer output of the agent's response")

        if st.button("Submit Query"):
            if user_query.strip() == "":
                st.warning("Please enter a query.")
            else:
                try:
                    # Show loading spinner while processing
                    with st.spinner('Processing your query...'):
                        # Get the response from the agent
                        response = data_analyst_agent.run(user_query)

                        # Extract the content from the response object
                        if hasattr(response, 'content'):
                            response_content = response.content
                        else:
                            response_content = str(response)

                    # Display the response in Streamlit
                    st.markdown(response_content)

                except Exception as e:
                    st.error(f"Error generating response from the agent: {e}")
                    st.error(
                        "Please try rephrasing your query or check if the data format is correct.")
