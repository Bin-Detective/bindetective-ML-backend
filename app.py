import os
import grpc
from concurrent import futures
from config import Config
import src.utils.model_utils as model_utils
import waste_prediction_pb2_grpc as waste_prediction_pb2_grpc
from src.grpc_handler import WastePredictionServicer, load_model_from_dir

# Check if the model directory exists
if not os.path.exists(Config.EXTRACTED_MODEL_DIR):
    # Download and extract the model
    model_utils.download_and_extract_model()

# Load the model
load_model_from_dir()

# Start the gRPC server
def serve():
    port = os.getenv('PORT', '443')
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    waste_prediction_pb2_grpc.add_WastePredictionServicer_to_server(
        WastePredictionServicer(), server
    )
    server.add_insecure_port(f"[::]:{port}")
    print("gRPC server is running on port 443")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()