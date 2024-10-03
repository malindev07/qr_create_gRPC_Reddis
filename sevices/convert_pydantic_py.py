from py_models.pydantic_models import QRRequestModelPydantic, QRResponseModelPydantic
from qr_models.qr_model import QRModelSearch, QRModelReturn


async def convert_pydantic_to_py(
    pydantic_model: QRRequestModelPydantic,
) -> QRModelSearch:
    return QRModelSearch(title=pydantic_model.title, url=pydantic_model.url)


async def convert_py_to_pydantic(py_model: QRModelReturn) -> QRResponseModelPydantic:
    # print(py_model)
    return QRResponseModelPydantic(title=py_model.title, status=py_model.status)
