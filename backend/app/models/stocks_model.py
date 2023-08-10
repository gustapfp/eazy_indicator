from beanie import Document, Indexed, Link, before_event, Replace, Insert
from uuid import UUID, uuid4
from typing import Optional
from pydantic import Field


class StocksModel(Document):
    stock_id: UUID = Field(default_factory=uuid4, unique=True)
    cotacao: float
    pl: float
    pvp: float
    psr: float
    dy: float
    pa: float
    pcg: float
    pebit: float
    pacl: float
    evebit: float
    evebitda: float
    mrgebit: float
    mrgliq: float
    roic: float
    roe: float
    liqc: float
    liq2m: float
    patrliq: float
    divbpatr: float
    c5y: float
    paper: str

    def __repr__(self) -> str:
            return f" -> Stock Paper: {self.example} <-" 
    
    def __str__(self) -> str:
        return self.paper
    