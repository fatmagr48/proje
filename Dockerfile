# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV APP_HOME /app

# Set work directory
WORKDIR $APP_HOME

# Install dependencies
COPY app/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY app/ .

# Create a non-root user and switch to it
RUN adduser --disabled-password --gecos '' appuser && chown -R appuser:appuser $APP_HOME
USER appuser

# Expose port
EXPOSE 5000

# Run the application
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "app:app"]
