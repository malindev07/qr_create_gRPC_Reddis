from py_models.pydantic_models import QRRequestModelPydantic, QRResponseModelPydantic
from qr_models.qr_model import QRModelSearch, QRModelReturn


async def convert_pydantic_to_py(
    pydantic_model: QRRequestModelPydantic,
) -> QRModelSearch:
    return QRModelSearch(title=pydantic_model.title, url=pydantic_model.url)


async def convert_py_to_pydantic(py_model: QRModelReturn) -> QRResponseModelPydantic:
    return QRResponseModelPydantic(title=py_model.title, qr=py_model.qr_image)
