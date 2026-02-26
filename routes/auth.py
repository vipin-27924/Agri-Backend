from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from database import ... 
from app.core.security import get_password_hash, verify_password, create_access_token
from app.models.user import UserSignUp

router = APIRouter()

@router.post("/signup")
async def signup(user: UserSignUp):
    # Check if phone already exists
    existing_user = await farmer_collection.find_one({"phone": user.phone})
    if existing_user:
        raise HTTPException(status_code=400, detail="Phone number already registered")
    
    # Hash password and save
    user_dict = user.dict()
    user_dict["hashed_password"] = get_password_hash(user_dict.pop("password"))
    await farmer_collection.insert_one(user_dict)
    return {"message": "Farmer registered successfully!"}

@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = await farmer_collection.find_one({"phone": form_data.username}) # Using phone as username
    if not user or not verify_password(form_data.password, user["hashed_password"]):
        raise HTTPException(status_code=401, detail="Invalid phone or password")
    
    token = create_access_token(data={"sub": user["phone"]})
    return {"access_token": token, "token_type": "bearer"}