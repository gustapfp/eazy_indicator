from fastapi import APIRouter, HTTPException, status
from schemas.stocks_schema import StockSchema, StocksSchemaResponse
from models.stocks_model import StocksModel
from typing import List
from services.stocks_services import StocksService
from uuid import UUID
stocks_router = APIRouter()

@stocks_router.post("/add_stock", summary='Add a stock to the buyer walet', status_code=status.HTTP_201_CREATED, response_model=StocksModel)
async def get_all_stocks_created(data: StockSchema):
    return await StocksService.create_stock(data=data)

@stocks_router.get("/", summary='Get a list with all stocks created', status_code=status.HTTP_200_OK, response_model=List[StocksSchemaResponse])
async def get_all_stocks_created():
    stocks = await StocksService.list_of_stocks() 
    
    return stocks

@stocks_router.get('/{id}', summary='Get a specific stock base on the id', status_code=status.HTTP_200_OK, response_model=StocksSchemaResponse)
async def get_stock_created(stock_id: UUID):
    stock = await StocksService.get_stock(stock_id)
    return stock

@stocks_router.put('/update_stock/{id}', summary='Update a specefic a stock based on the id', status_code=status.HTTP_200_OK, response_model=StocksSchemaResponse)
async def update_stock(stock_id: UUID, data: StocksSchemaResponse):
    stock = await StocksService.update_stock(stock_id=stock_id, data=data)
    return stock

@stocks_router.delete('/delete_stock/{id}',summary= 'Update a specefic a stock based on the id', status_code=status.HTTP_204_NO_CONTENT)
async def delete_stock(stock_id:UUID):
    await StocksService.delete_stock(stock_id)
    