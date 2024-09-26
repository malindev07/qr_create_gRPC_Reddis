from signal import SIGINT

from grpc import aio

from protos import qr_pb2_grpc, qr_pb2
from qr_models.qr_create import qr_create


class QRServicer(qr_pb2_grpc.QRServiceServicer):
    async def CreateQR(self, request, context) -> qr_pb2.CreateQRResponse:
        qr = await qr_create(
            title=request.title, url=request.url, completed=request.completed
        )
        return qr_pb2.CreateQRResponse(qr=qr)


async def run_server(qr_server_addr: str) -> None:
    server = aio.server()
    try:

        qr_pb2_grpc.add_QRServiceServicer_to_server(
            servicer=QRServicer(), server=server
        )

        server.add_insecure_port(qr_server_addr)
        print(f"Run QRServicer on {qr_server_addr} ")
        await server.start()
        await server.wait_for_termination()
    finally:
        await server.stop(grace=SIGINT)
