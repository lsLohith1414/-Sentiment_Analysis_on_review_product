# Use Python 3.11 slim as base
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy backend dependencies
COPY requirements_backend.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements_backend.txt

# Install spaCy
RUN pip install --no-cache-dir spacy==3.7.1

# Download spaCy large English model separately
RUN python -m spacy download en_core_web_lg --direct

# Copy backend application code
COPY . .

# Expose backend port
EXPOSE 8000

# Start FastAPI app with uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
