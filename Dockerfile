FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy requirements first for better caching
COPY requirements.txt /app/

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ /app/src/

# Expose port 5000
EXPOSE 5000

# Create non-root user for security
RUN adduser --disabled-password --gecos "" --shell /bin/false appuser
USER appuser

# Run the application
CMD ["python", "src/datetime_api.py"]