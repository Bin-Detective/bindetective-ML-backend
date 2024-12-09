# Robin FastAPI Service

## Table of Contents

1. [Project Introduction](#project-introduction)
2. [Project Structure](#project-structure)

## Project Introduction

The Bindetective ML Service Backend is a dedicated service for machine learning-based waste image prediction, integrated into the Bin Detective app. Built using the FastAPI framework, this service is designed to handle real-time image predictions for waste classification. The service accepts image URLs, downloads the images, and utilizes a pre-trained machine learning model to classify the waste type.

The service is deployed on Google Cloud Run, ensuring scalable, serverless execution. It utilizes a custom model handler, WastePredictionServicer, which is responsible for running the prediction logic based on the input image. The app also includes robust error handling, logging, and a clean API interface to interact with the frontend of the Bin Detective app.

The backend is designed for efficiency, scalability, and security, providing high-performance predictions with minimal overhead. It seamlessly integrates with other services within the Bin Detective ecosystem, including the Express-based backend, ensuring a smooth flow of data and functionality across the platform.

## Project Structure

```plain
project_root/
│
├── src/
│   ├── utils/
│   │   └── model_utils.py
│   └── handler.py
│
├── .env
├── config.py Set static environment variables here
├── requirements.txt] Package dependencies, Use Python 3.10
├── Dockerfile
├── .gitignore
└── app.py
```
