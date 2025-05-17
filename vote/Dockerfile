FROM python:3.11-slim

# Install system dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends curl && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /usr/local/app

# Copy requirements first for better caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Runtime configuration
EXPOSE 8080
CMD ["gunicorn", "app:app", "-b", "0.0.0.0:8080", \
     "--log-file", "-", \
     "--access-logfile", "-", \
     "--workers", "4", \
     "--keep-alive", "0"]
