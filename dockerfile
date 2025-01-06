FROM python:latest

# Install Flask
RUN pip install flask

# Copy the application code
COPY test.py /app/test.py

# Set the working directory
WORKDIR /app

# Expose the port Flask will run on
EXPOSE 5000

# Run the application
CMD ["python", "test.py"]
