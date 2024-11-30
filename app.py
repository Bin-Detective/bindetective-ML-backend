import os

# Set the environment variable
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'

import logging
import requests
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from config import Config
import src.utils.model_utils as model_utils
from src.handler import WastePredictionServicer, load_model_from_dir


# Load the model
load_model_from_dir()

# Initialize FastAPI app
app = FastAPI()

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class ImageURL(BaseModel):
    url: str

@app.post("/predict")
async def predict(image_url: ImageURL):
    try:
        # Download the image
        response = requests.get(image_url.url)
        response.raise_for_status()
        image_bytes = response.content
        logger.info("Image downloaded successfully from URL.")
        
        # Assuming WastePredictionServicer is defined elsewhere and has a predict method
        servicer = WastePredictionServicer()
        prediction = servicer.predict(image_bytes)
        logger.info("Prediction made successfully.")
        
        return prediction
    except requests.exceptions.RequestException as e:
        logger.error(f"Error downloading image: {e}")
        raise HTTPException(status_code=400, detail="Error downloading image")
    except FileNotFoundError as e:
        logger.error(f"File not found: {e}")
        raise HTTPException(status_code=404, detail="File not found")
    except ValueError as e:
        logger.error(f"Value error: {e}")
        raise HTTPException(status_code=400, detail="Invalid input")
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        raise HTTPException(status_code=500, detail="Internal server error")

# Start the FastAPI server
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv('PORT', '7976'))
    uvicorn.run(app, host='0.0.0.0', port=port)