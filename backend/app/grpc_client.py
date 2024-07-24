import grpc
import service_pb2
import service_pb2_grpc
import logging

def get_data_from_db():
    try:
        with grpc.insecure_channel('grpc_service:50051') as channel:
            stub = service_pb2_grpc.DatabaseServiceStub(channel)
            request = service_pb2.Empty()
            metadata = (('cache-control', 'no-cache, no-store, must-revalidate'),)
            response = stub.GetData(request, metadata=metadata, timeout=5)
            return [{"id": item.id, "text": item.text} for item in response.data]
    except grpc.RpcError as e:
        logging.info(f"gRPC error: {e}")
        return [{"id": 1, "text":f"gRPC error: {e}"}]
