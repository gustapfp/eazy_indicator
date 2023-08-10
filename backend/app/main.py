from fastapi import FastAPI
from core.config import settings
from beanie import init_beanie 
from motor.motor_asyncio import AsyncIOMotorClient
from models.stocks_model import StocksModel
from api.api_v1.router import router
from fastapi.middleware.cors import CORSMiddleware


tags_metadata = [
    {
        "name": "stocks",
        "description": "Operations with stocks.",
    },
    
]



app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    openapi_tags=tags_metadata
)

app.include_router(
    router=router
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.BACKEND_CORS_ORIGINS,
    allow_credentials=True,
    allow_methods=['*'], 
    allow_headers=['*']
)

@app.on_event('startup')
async def app_init():
    client_db = AsyncIOMotorClient(settings.MONGO_CONNECTION_STRING).ei
    await init_beanie(
        database= client_db,
        document_models=[
            StocksModel,
        ]
    )