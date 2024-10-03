import os
import pathlib
import time
import typing
import webbrowser

import qrcode
from google.protobuf.json_format import MessageToDict


from client.client import grpc_qr_client
from protos import qr_pb2
from qr_models.qr_model import QRModelSearch, QRModelReturn


async def create_qr_picture(qr_model: QRModelReturn) -> None:

    img = qrcode.make(qr_model.url)

    path: str = f"qrs/{qr_model.title}.png"

    img.save(path)

    # html_content = f"""
    #    <!DOCTYPE html>
    #    <html>
    #    <head>
    #        <title>'Test'</title>
    #    </head>
    #    <body>
    #        <h1>{qr_model.title}</h1>
    #        <h1>{qr_model.url}</h1>
    #        <img src={path} alt="альтернативный текст">
    #    </body>
    #    </html>
    #    """
    #
    # with open(f"qrs/{qr_model.title}.html", "w") as f:
    #
    #     f.write(html_content)

    # webbrowser.open("file://" + os.path.realpath(path))
    os.system(f"start {path}")


async def create_qr(
    qr: QRModelSearch, client: typing.Any = grpc_qr_client
) -> QRModelReturn:
    qr_grpc = await client.CreateQR(
        qr_pb2.CreateQRRequest(title=qr.title, url=qr.url), timeout=5
    )

    data_grpc = MessageToDict(qr_grpc)

    new_qr = QRModelReturn(
        title=data_grpc["qr"]["title"],
        url=data_grpc["qr"]["url"],
        status="created",
    )

    await create_qr_picture(qr_model=new_qr)
    return new_qr
