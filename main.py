from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes import market
app.include_router(market.router, prefix="/markets", tags=["Markets"])
from routes import auth 


app = FastAPI()

app.include_router(auth.router, prefix="/auth", tags=["Authentication"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {
        "status": "online",
        "message": "Welcome to AgriConnect API",
        "features": ["Mandi Prices", "Tractor Rental", "Gemini Advisory"]
    }

