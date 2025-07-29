from pydantic import BaseModel
from enum import Enum

class OrderStatus(str, Enum):
    pass

class OrderUpdate(BaseModel):
    pass

class OrderResponse(BaseModel):
    pass
