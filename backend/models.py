"""
Pydantic Models for DigiKazi
- User, Gig, Tender, Equipment, Ride, Emergency
- TODO: Add trust/safety, analytics, and language support fields
"""

from pydantic import BaseModel, Field
from typing import Optional, List

class User(BaseModel):
    id: str
    name: str
    phone: str
    skills: List[str]
    location: str
    role: str  # fundi, rider, SME, etc.
    rating: Optional[float]
    language: Optional[str] = "en"  # TODO: Support Swahili/Sheng
    # TODO: Add KYC, trust/safety fields

class Gig(BaseModel):
    id: str
    title: str
    description: str
    location: str
    pay: float
    posted_by: str  # user id
    is_active: bool
    # TODO: Add analytics, reminders

class Tender(BaseModel):
    id: str
    title: str
    pdf_url: str
    deadline: str
    requirements: Optional[str]
    # TODO: Add parsed fields, reminders

class Equipment(BaseModel):
    id: str
    name: str
    owner_id: str
    is_available: bool
    location: str
    # TODO: Add QR code, geo-tracking

class Ride(BaseModel):
    id: str
    rider_id: str
    passenger_id: str
    start_location: str
    end_location: str
    status: str
    # TODO: Add group rides, scheduled rides

class Emergency(BaseModel):
    id: str
    user_id: str
    type: str
    location: str
    timestamp: str
    # TODO: Add trusted contacts, panic button

class EmergencyRequest(BaseModel):
    user_id: str
    location: str
    type: str  # e.g., "medical", "breakdown" 