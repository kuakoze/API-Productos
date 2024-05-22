### Product model ###

from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    _id: Optional[str]
    nombre: str
    descripcion: str
    precio: float
    categoria: str
    stock: int




