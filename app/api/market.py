from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_market_prices():
    return {
        "rice": "₹2200/quintal",
        "wheat": "₹2100/quintal",
        "cotton": "₹6000/quintal"
    }
