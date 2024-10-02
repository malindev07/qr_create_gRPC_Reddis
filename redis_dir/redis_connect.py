import asyncio
import typing

import redis
from fastapi import Depends

from client.client import grpc_qr_client
from qr_models.qr_model import QRModelSearch
from sevices.create_qr import create_qr


async def check_data(
    qr_data: QRModelSearch, client: typing.Any = Depends(grpc_qr_client)
):
    with redis.Redis(
        host="127.0.0.1", port=6379, db=0, decode_responses=True
    ) as redis_client:

        res: str | None = redis_client.get(qr_data.title)

        if res is not None:
            data = res
            print(
                f"QR с названием {qr_data.title} уже существует, мы достали его из Redis"
            )

        else:
            data = await create_qr(qr=qr_data, client=client)
            print(data)
            print(
                f"QR с названием {qr_data.title} не существует, мы передали задачу worker через gRPC"
            )
            redis_client.set(data.title, data.qr_image)

        return data


# asyncio.run(check_data("1"))
