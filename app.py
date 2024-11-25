import os
from fastapi import FastAPI, UploadFile, File, HTTPException
from config import Config
import src.utils.model_utils as model_utils
from src.handler import WastePredictionServicer, load_model_from_dir

# Load the model
load_model_from_dir()

# Initialize FastAPI app
app = FastAPI()

# Define a route for prediction
@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    try:
        image_bytes = await file.read()
        servicer = WastePredictionServicer()
        prediction = servicer.predict(image_bytes)
        return prediction
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Start the FastAPI server
if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv('PORT', '5000'))
    uvicorn.run(app, host='0.0.0.0', port=port)