# Use Python base image
FROM python:3.9

# Set the working directory
WORKDIR /usr/src/app

# Copy requirements and install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 5000 and start the Flask app
EXPOSE 5000
CMD ["python", "app.py"]
