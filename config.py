import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    EXTRACTED_MODEL_DIR = os.path.join(os.getcwd(), 'model_dir')
    TF_ENABLE_ONEDNN_OPTS = os.getenv('TF_ENABLE_ONEDNN_OPTS', '0')

