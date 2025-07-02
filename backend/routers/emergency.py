"""
Emergency Router
- Endpoints for emergency dispatch, trusted contacts, panic button, analytics
- Integrates reminders, trust/safety
"""

from fastapi import APIRouter, BackgroundTasks
from backend.models import Emergency
from typing import List
# from backend.db import supabase

router = APIRouter(prefix="/emergency", tags=["emergency"])

emergencies_db = []  # TODO: Replace with Supabase DB

@router.post("/dispatch", response_model=Emergency)
def dispatch_emergency(emergency: Emergency, background_tasks: BackgroundTasks):
    """Dispatch emergency and notify trusted contacts"""
    emergencies_db.append(emergency)
    # TODO: Insert into Supabase
    # TODO: Notify trusted contacts via WhatsApp
    background_tasks.add_task(lambda: print(f"Notify trusted contacts for {emergency.user_id}"))
    return emergency

@router.get("/", response_model=List[Emergency])
def list_emergencies():
    """List all emergencies"""
    return emergencies_db

@router.get("/analytics")
def emergency_analytics():
    """Return emergency analytics (stub)"""
    # TODO: Implement real analytics
    return {"total_emergencies": len(emergencies_db)}

# TODO: Add panic button, reminders, trust/safety checks 