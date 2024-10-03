import asyncio
import typing

import redis
from fastapi import Depends

from client.client import grpc_qr_client
from qr_models.qr_model import QRModelSearch, QRModelReturn
from settings.redis_settings import HOST, PORT, DECODE_RESPONSES, DB
from sevices.create_qr import create_qr, create_qr_picture


async def check_data(
    qr_data: QRModelSearch, client: typing.Any = Depends(grpc_qr_client)
) -> QRModelReturn:
    with redis.Redis(
        host=HOST, port=PORT, db=DB, decode_responses=DECODE_RESPONSES
    ) as redis_client:

        res = redis_client.hset(qr_data.title, "title", qr_data.title)

        if res == 0:
            res = redis_client.hgetall(qr_data.title)

            data = QRModelReturn(
                title=res["title"], url=qr_data.url, status=res["status"]
            )
            print(
                f"QR с названием {qr_data.title} уже существует, мы достали его из Redis"
            )
            await create_qr_picture(qr_model=data)

        else:
            data = await create_qr(qr=qr_data, client=client)

            print(
                f"QR с названием {qr_data.title} не существует, мы передали задачу worker через gRPC"
            )

            redis_client.hset(
                qr_data.title,
                mapping={
                    "title": qr_data.title,
                    "url": qr_data.url,
                    "status": data.status,
                },
            )

        redis_client.close()

        return data


# asyncio.run(check_data("1"))
