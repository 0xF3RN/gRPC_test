import asyncio
import logging

import grpc # type: ignore
import service_pb2
import service_pb2_grpc

from db import get_data
#from data_test import get_data # mainly for tests

_cleanup_coroutines = []

class DatabaseService(service_pb2_grpc.DatabaseServiceServicer):

    async def GetData(self, request, context):
        logging.info(f"Request has been recieved")
        data = get_data()
        response = service_pb2.DataResponse()
        for item in data:
            response.data.add(id=item['id'], text=item['text'])
        logging.info(response)
        return response


async def serve() -> None:
    server = grpc.aio.server()
    service_pb2_grpc.add_DatabaseServiceServicer_to_server(DatabaseService(), server)
    server.add_insecure_port('[::]:50051')
    logging.info("Starting server on port 50051")
    await server.start()
    async def server_graceful_shutdown():
        logging.info("Starting GRACEFUL shutdown...")
        await server.stop(5)
    _cleanup_coroutines.append(server_graceful_shutdown())
    await server.wait_for_termination()


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(serve())
    finally:
        loop.run_until_complete(*_cleanup_coroutines)
        loop.close()