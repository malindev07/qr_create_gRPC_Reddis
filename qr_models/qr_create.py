from protos.qr_pb2 import QR


async def qr_create(title: str, url: str, completed: bool) -> QR:
    qr = QR(title=title, url=url, completed=completed)
    print(f"New QR Created {qr.title}")
    return qr
