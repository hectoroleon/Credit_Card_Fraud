# Use an official Python 3.11 runtime as base image
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose the port where the app runs
EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]