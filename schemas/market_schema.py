from fastapi import APIRouter
import requests

router = APIRouter()

@router.get("/today")
async def get_market_rates(state: str, district: str):
    # This is where you call the Data.gov.in API
    # For now, return a mock response so your Android team can build the UI
    return [
        {"item": "Wheat", "price": "2400", "unit": "Quintal", "mandi": "Noida"},
        {"item": "Potato", "price": "1200", "unit": "Quintal", "mandi": "Greater Noida"}
    ]
    