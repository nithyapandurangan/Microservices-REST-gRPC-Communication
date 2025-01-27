#gRPC Processor
# This is the processor service. It processes the data and sends it to the aggregator service.
from concurrent import futures
import grpc
import services_pb2
import services_pb2_grpc
from grpc_reflection.v1alpha import reflection  

class ProcessorService(services_pb2_grpc.ProcessorServiceServicer):
    def Process(self, request, context):
        return services_pb2.ProcessedData(result=f"Processed: {request.content}")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_ProcessorServiceServicer_to_server(ProcessorService(), server)
    server.add_insecure_port('[::]:50052')

    # Enable reflection for the server
    SERVICE_NAMES = (
        services_pb2.DESCRIPTOR.services_by_name['ProcessorService'].full_name,
        reflection.SERVICE_NAME,  
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()

