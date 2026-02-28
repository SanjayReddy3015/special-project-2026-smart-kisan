from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api import community, weather, market
from app.database import connect_to_mongo, close_mongo_connection

app = FastAPI(
    title="WikiKisan API",
    version="1.0.0"
)

# CORS (important for frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await connect_to_mongo()

@app.on_event("shutdown")
async def shutdown():
    await close_mongo_connection()

@app.get("/")
async def root():
    return {"message": "WikiKisan Backend Running 🚜"}

@app.get("/health")
async def health():
    return {"status": "ok"}

# Routers
app.include_router(community.router, prefix="/api/community", tags=["Community"])
app.include_router(weather.router, prefix="/api/weather", tags=["Weather"])
app.include_router(market.router, prefix="/api/market", tags=["Market"])
