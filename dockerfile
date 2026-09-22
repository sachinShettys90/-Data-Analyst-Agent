# Use Python 3.12 because your pyproject.toml requires Python >= 3.12
FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Start Streamlit application
CMD ["streamlit", "run", "DataAnalyst_Agent.py", "--server.address=0.0.0.0", "--server.port=8501"]