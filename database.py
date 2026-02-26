from motor.motor_asyncio import AsyncIOMotorClient
import os


MONGO_DETAILS = os.getenv("MONGO_URL", "localhost:27017")

client = AsyncIOMotorClient(MONGO_DETAILS)
database = client.agriconnect_db


farmer_collection = database.get_collection("farmers")
rental_collection = database.get_collection("rentals")