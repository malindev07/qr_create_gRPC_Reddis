import random

from protos.qr_pb2 import QR
from qr_models.qr_model import QRModelSearch


def convert_pymodel_to_grpc(qr_model: QRModelSearch):
    qr_response = QR(
        id=random.randint(1, 1000),
        title=qr_model.title,
        url=qr_model.url,
    )

    return
