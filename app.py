import os
import grpc
from concurrent import futures
from config import Config
import src.utils.model_utils as model_utils
import waste_prediction_pb2_grpc as waste_prediction_pb2_grpc
from src.grpc_handler import WastePredictionServicer, load_model_from_dir

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
    print(f"gRPC server is running on port {port}")
    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()