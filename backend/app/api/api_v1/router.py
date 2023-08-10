from fastapi import APIRouter
from handlers.stocks_handlers import stocks_router

router = APIRouter()

router.include_router(
    prefix='/stocks',
    tags='[stocks]'
)