# Use Python 3.11 slim as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy frontend dependencies
COPY requirements_frontend.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements_frontend.txt

# Copy frontend app code
COPY . .

# Expose frontend port
EXPOSE 8501

# Start Streamlit app
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0", "--server.port=8501"]
