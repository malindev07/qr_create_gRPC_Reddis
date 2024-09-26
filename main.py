import typing

from fastapi import FastAPI, Depends
from google.protobuf.json_format import MessageToDict
from starlette import status
from starlette.responses import JSONResponse

from client.client import grpc_qr_client
from protos import qr_pb2

app = FastAPI()


@app.get("/test")
async def test():
    return {"test": "test"}


@app.post("/", status_code=status.HTTP_201_CREATED)
async def create_qr(
    title: str, url: str, completed: bool, client: typing.Any = Depends(grpc_qr_client)
) -> JSONResponse:
    qr = await client.CreateQR(
        qr_pb2.CreateQRRequest(title=title, url=url, completed=completed), timeout=5
    )
    return JSONResponse(MessageToDict(qr))
