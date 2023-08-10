from fastapi import APIRouter
from schemas.stocks_schema import StockSchema, StocksSchemaDetail
import pymongo

stocks_router = APIRouter()

