#gRPC Aggregator
# This is the aggregator service. It aggregates the data from the processor service.
from concurrent import futures
import grpc
import services_pb2
import services_pb2_grpc
from grpc_reflection.v1alpha import reflection  # Import reflection

class AggregatorService(services_pb2_grpc.AggregatorServiceServicer):
    def Aggregate(self, request_iterator, context):
        summary = []
        for data in request_iterator:
            summary.append(data.result)
        return services_pb2.Summary(summary=" | ".join(summary))

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    services_pb2_grpc.add_AggregatorServiceServicer_to_server(AggregatorService(), server)
    server.add_insecure_port('[::]:50053')

    # Enable reflection for the server
    SERVICE_NAMES = (
        services_pb2.DESCRIPTOR.services_by_name['AggregatorService'].full_name,
        reflection.SERVICE_NAME,  # Add reflection service to the list of services
    )
    reflection.enable_server_reflection(SERVICE_NAMES, server)

    server.start()
    server.wait_for_termination()

if __name__ == "__main__":
    serve()
