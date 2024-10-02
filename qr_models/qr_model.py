from dataclasses import dataclass


@dataclass
class QRModelSearch:
    title: str
    url: str


@dataclass
class QRModelReturn:
    title: str
    qr_image: str
