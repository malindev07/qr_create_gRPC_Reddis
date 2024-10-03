import asyncio

from settings.grpc_settings import QR_GRPC_SERVER_ADDR
from sevices.qr import run_server


try:
    asyncio.run(run_server(QR_GRPC_SERVER_ADDR))
except KeyboardInterrupt:
    print("Exit")
finally:
    print("Stop server")
