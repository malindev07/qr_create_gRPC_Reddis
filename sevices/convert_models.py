import random

from protos.qr_pb2 import QR
from qr_models.qr_model import QRModel


def convert_pymodel_to_grpc(qr_model: QRModel):
    qr_response = QR(
        id=random.randint(1, 1000),
        title=qr_model.title,
        url=qr_model.url,
        completed=qr_model.completed,
    )

    return
