from fastapi import APIRouter
from api.api_v1.handlers.stocks_handlers import stocks_router

router = APIRouter()

router.include_router(
    router=stocks_router,
    prefix='/stocks',
    tags=['stocks']
)