from pydantic import BaseModel, Field
from pydantic.types import Decimal
from typing import Optional

class StockSchema(BaseModel):
    price: Decimal = Field(..., decimal_places=3)
    purchase_price: Decimal = Field(..., mdecimal_places=3)
    paper: str = Field(..., max_length=7)
    stock_exchange: Optional[str]  = Field(..., max_length=7)


class StocksSchemaResponse(BaseModel):
    price: float
    purchase_price: float
    paper: str
    stock_exchange: Optional[str]
    