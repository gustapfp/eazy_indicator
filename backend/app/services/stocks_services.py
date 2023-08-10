from schemas.stocks_schema import StockSchema, StocksSchemaResponse
from models.stocks_model import StocksModel
from typing import List
from uuid import UUID
from fastapi import HTTPException, status


class StocksService:
    @staticmethod
    async def create_stock(data: StockSchema) -> StocksModel:
        new_stock = StocksModel(**dict(data))
        
        return await new_stock.insert()
        

    @staticmethod
    async def list_of_stocks() -> List[StocksModel]:
        stocks_list = await StocksModel.find().to_list()
        if not stocks_list:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="There aren't any stocks registered")
        return stocks_list
    
    @staticmethod
    async def get_stock(stock_id: UUID) -> StocksModel:
        stock = await StocksModel.find_one(stock_id== StocksModel.stock_id)
        if not stock:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Thease stock doens't exist.")
        return stock
    
    @staticmethod
    async def update_stock(stock_id: UUID, data:StockSchema) -> StockSchema:
        stock = await StocksService.get_stock(stock_id)
        if not stock:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You are trying to update a stock that doens't exist.")
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
        if not stock:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="You are trying to delete a stock that doens't exist or is already deleted.")
        return await stock.delete()