import grpc.aio
from protos import qr_pb2_grpc

from settings import QR_GRPC_SERVER_ADDR


async def grpc_qr_client():
    channel = grpc.aio.insecure_channel(QR_GRPC_SERVER_ADDR)
    client = qr_pb2_grpc.QRServiceStub(channel)
    return client
