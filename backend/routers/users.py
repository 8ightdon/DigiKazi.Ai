"""
Users Router
- Endpoints for user registration, login, KYC, profile management, ratings, reviews, analytics
- Integrates language support, trust/safety
"""

from fastapi import APIRouter, HTTPException
from backend.models import User
from typing import List
# from backend.db import supabase

router = APIRouter(prefix="/users", tags=["users"])

users_db = []  # TODO: Replace with Supabase DB

@router.get("/", response_model=List[User])
def list_users():
    """List all users"""
    return users_db

@router.post("/register", response_model=User)
def register_user(user: User):
    """Register a new user"""
    users_db.append(user)
    # TODO: Insert into Supabase
    return user

@router.post("/login")
def login_user(phone: str):
    """Login user by phone (stub)"""
    # TODO: Implement real auth
    user = next((u for u in users_db if u.phone == phone), None)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

@router.get("/analytics")
def users_analytics():
    """Return user analytics (stub)"""
    # TODO: Implement real analytics
    return {"total_users": len(users_db)}

# TODO: Add KYC, ratings, reviews, language support, trust/safety checks

# TODO: Add endpoints for registration, KYC, trust/safety, analytics 