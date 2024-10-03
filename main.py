import typing

import uvicorn
from fastapi import FastAPI, Depends
from google.protobuf.json_format import MessageToDict
from starlette import status
from starlette.responses import JSONResponse

from client.client import grpc_qr_client
from protos import qr_pb2
from py_models.pydantic_models import QRRequestModelPydantic, QRResponseModelPydantic
from qr_models.qr_model import QRModelReturn
from redis_dir.redis_connect import check_data
from sevices.convert_pydantic_py import convert_pydantic_to_py, convert_py_to_pydantic

app = FastAPI()


@app.post("/create_qr", status_code=status.HTTP_201_CREATED)
async def create_qr(
    qr: QRRequestModelPydantic, client: typing.Any = Depends(grpc_qr_client)
) -> QRResponseModelPydantic:

    res: QRModelReturn = await check_data(
        await convert_pydantic_to_py(qr), client=client
    )

    new_qr = await convert_py_to_pydantic(res)

    return new_qr


if __name__ == "__main__":
    uvicorn.run("main:app", reload=True)
