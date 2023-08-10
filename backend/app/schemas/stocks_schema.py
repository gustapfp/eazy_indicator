from pydantic import BaseModel, Field


class StockSchema(BaseModel):
    paper:str
    cotacao:float

class StocksSchemaDetail(BaseModel):
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
