from pprint import pprint

from pydantic import BaseModel
import sys
pprint(sys.path)

class ProductBase(BaseModel):
    name: str
    # description: str
    # price: float

class ProductCreate(ProductBase):
    pass

class Product(ProductBase):
    id: int

    class Config:
        orm_mode = True
