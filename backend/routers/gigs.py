"""
Gigs Router
- Endpoints for posting, listing, and matching gigs
- Integrates AI matching, reminders, analytics, trust/safety
"""

from fastapi import APIRouter, HTTPException, BackgroundTasks
from backend.models import Gig, User
from typing import List
# from backend.ai.matching import match_user_to_gig
# from backend.db import supabase

router = APIRouter(prefix="/gigs", tags=["gigs"])

gigs_db = []  # TODO: Replace with Supabase DB

@router.get("/", response_model=List[Gig])
def list_gigs():
    """List all gigs"""
    return gigs_db

@router.post("/", response_model=Gig)
def post_gig(gig: Gig):
    """Post a new gig"""
    gigs_db.append(gig)
    # TODO: Insert into Supabase
    return gig

@router.post("/match", response_model=List[Gig])
def match_gigs(user: User):
    """AI-powered gig matching for a user"""
    # TODO: Use OpenAI embeddings for semantic match
    # matches = match_user_to_gig(user, gigs_db)
    matches = gigs_db[:2]  # Dummy: return first 2
    return matches

@router.post("/reminder")
def set_gig_reminder(gig_id: str, user_id: str, background_tasks: BackgroundTasks):
    """Set a reminder for a gig deadline"""
    # TODO: Schedule WhatsApp reminder
    background_tasks.add_task(lambda: print(f"Reminder for gig {gig_id} to user {user_id}"))
    return {"status": "reminder set"}

@router.get("/analytics")
def gig_analytics():
    """Return gig analytics (stub)"""
    # TODO: Implement real analytics
    return {"total_gigs": len(gigs_db)}

# TODO: Add trust/safety checks, reviews, ratings

# TODO: Add endpoints for posting gigs, AI matching, reminders 