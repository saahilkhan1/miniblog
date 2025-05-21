# Use official Python image as base
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies for PostgreSQL and pip
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the code
COPY . .

# Collect static files (if using)
# RUN python manage.py collectstatic --noinput

# Expose port 8000 (Django default)
EXPOSE 8000

# Run migrations and start server by default
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
