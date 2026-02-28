from fastapi import APIRouter
from app.database import get_database

router = APIRouter()

@router.get("/")
async def get_posts():
    db = get_database()
    posts = await db.posts.find().to_list(100)
    return posts

@router.post("/")
async def create_post(post: dict):
    db = get_database()
    await db.posts.insert_one(post)
    return {"message": "Post created"}
