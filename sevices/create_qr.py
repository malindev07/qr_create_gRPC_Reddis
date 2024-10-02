import typing

from fastapi import Depends
from google.protobuf.json_format import MessageToDict
from starlette.responses import JSONResponse

from client.client import grpc_qr_client
from protos import qr_pb2
from qr_models.qr_model import QRModelSearch, QRModelReturn


async def create_qr(qr: QRModelSearch, client: typing.Any = Depends(grpc_qr_client)):
    qr = await client.CreateQR(
        qr_pb2.CreateQRRequest(title=qr.title, url=qr.url), timeout=5
    )

    data_redis = MessageToDict(qr)
    print(data_redis)
    new_qr = QRModelReturn(title=data_redis["qr"]["title"], qr_image="123")
    return new_qr
