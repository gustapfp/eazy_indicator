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
    async def list_of_stocks() -> List[StocksModel]:
        stocks_list = await StocksModel.find().to_list()
        return stocks_list
    
    @staticmethod
    async def get_stock(stock_id: UUID) -> StocksModel:
        stock = await StocksModel.find_one(stock_id== StocksModel.stock_id)
        return stock
    
    @staticmethod
    async def update_stock(stock_id: UUID, data:StockSchema) -> StockSchema:
        stock = await StocksService.get_stock(stock_id)
        await stock.update({
            '$set': data.dict(
                exclude_unset=True
            )   
        })
        await stock.save()
        return stock
    
    @staticmethod
    async def delete_stock(stock_id: UUID):
        stock = await StocksService.get_stock(stock_id)
        return await stock.delete()