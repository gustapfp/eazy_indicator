from fastapi import APIRouter, HTTPException, status
from schemas.stocks_schema import StockSchema, StocksSchemaResponse
from services.stocks_services import StocksService
import pymongo

stocks_router = APIRouter()

@stocks_router.post("/add_stock", summary='Add a stock to the buyer walet', status_code=status.HTTP_201_CREATED, response_model=StocksSchemaResponse)
async def get_all_stocks_created(data: StockSchema):
    return await StocksService.create_stock(data=data)

@stocks_router.get("/", summary='Get a list with all stocks created', status_code=status.HTTP_200_OK)
async def get_all_stocks_created():
    stocks = await StocksService.list_of_stocks_created() 
    return stocks
