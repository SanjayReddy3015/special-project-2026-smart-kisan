import os
from motor.motor_asyncio import AsyncIOMotorClient

client = None
db = None

async def connect_to_mongo():
    global client, db
    MONGO_URL = os.getenv("MONGO_URL")
    client = AsyncIOMotorClient(MONGO_URL)
    db = client.wikikisan

async def close_mongo_connection():
    global client
    if client:
        client.close()

def get_database():
    return db
