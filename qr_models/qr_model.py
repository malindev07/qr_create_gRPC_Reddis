from dataclasses import dataclass


@dataclass
class QRModel:
    title: str
    url: str
    completed: bool
