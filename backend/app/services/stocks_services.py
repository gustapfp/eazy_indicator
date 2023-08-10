from schemas.stocks_schema import StockSchema, StocksSchemaResponse
from models.stocks_model import StocksModel
from typing import List
from uuid import UUID



class StocksService:
    @staticmethod
    async def create_stock(data: StockSchema) -> StocksModel:
        new_stock = StocksModel(**dict(data))
        return await new_stock.insert()
        

    @staticmethod
    async def list_of_stocks_created() -> List[StocksModel]:
        stocks_list = await StocksModel.find_all().to_list()
        return stocks_list
    
    