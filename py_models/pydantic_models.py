from dataclasses import dataclass


@dataclass
class QRRequestModelPydantic:
    title: str
    url: str


@dataclass
class QRResponseModelPydantic:
    title: str
    status: str
