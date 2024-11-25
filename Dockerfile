# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Install grpcio-tools for generating gRPC files
RUN pip install grpcio-tools

# Copy the current directory contents into the container at /app
COPY . .

# Expose port 50051 for the gRPC server
EXPOSE 443

# Run the application
CMD ["python", "app.py"]

# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set the working directory
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Download and extract the model
RUN python -c "from config import Config; import src.utils.model_utils as model_utils; model_utils.download_and_extract_model()"

# Expose the port that the gRPC server will run on
EXPOSE 443

# Command to run the gRPC server
CMD ["python", "app.py"]