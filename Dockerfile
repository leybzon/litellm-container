# Use a lightweight Python base image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the local application files to the working directory
# This includes the .env file for environment variables
COPY . .

# Install dependencies with pip, including python-dotenv for handling .env files
RUN pip install --no-cache-dir flask litellm python-dotenv

# Ensure the .env file is copied and accessible inside the container
# This file contains sensitive API keys, so it should be secured
COPY .env /app/.env

# Expose the port on which the application will run
# Flask defaults to port 5000, but we're using 8080 as per our configuration
EXPOSE 8080

# Set the entry point to run the Flask application
# This command starts the app using Python
ENTRYPOINT ["python", "main.py"]

