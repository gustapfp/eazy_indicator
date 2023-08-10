from beanie import Document, Indexed, Link, before_event, Replace, Insert
from uuid import UUID, uuid4
from typing import Optional
from pydantic import Field


class StocksModel(Document):
    stock_id: UUID = Field(default_factory=uuid4, unique=True)
    price: float
    purchase_price: float
    paper: str
    stock_exchange: Optional[str]


    def __repr__(self) -> str:
            return f" -> Stock Paper: {self.paper} <-" 
    
    def __str__(self) -> str:
        return self.paper
    