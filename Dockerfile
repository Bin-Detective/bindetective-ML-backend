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
RUN python -c "from config import Config; import src.utils.model_utils as model_utils; model_utils.download_and_extract_model('https://www.kaggle.com/api/v1/models/bahiskaraananda/robin-resnet50/tensorFlow2/1.1-23m/1/download')"

# Expose the port that the gRPC server will run on
EXPOSE 443

# Command to run the gRPC server
CMD ["python", "app.py"]