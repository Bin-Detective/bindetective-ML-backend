# Robin FastAPI Service

A FastAPI-based service for our waste prediction model, Robin. The service downloads the model from Kaggle, extracts it, and uses it to make predictions on waste images.

This service is designed to run as a subsidiary for our backend app in Google Cloud Run, enabling a high-performance microservice architecture.

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
├── [config.py](http://_vscodecontentref_/1)
├── [requirements.txt](http://_vscodecontentref_/2)
├── Dockerfile
├── .gitignore
└── [app.py](http://_vscodecontentref_/3)
```
