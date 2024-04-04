from typing import Union
from pydantic import BaseModel

items = []

# Model in MVC
class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None