"""
DigiKazi AI-Bot Backend Entrypoint (Unified & Modular)
- Imports and includes all routers
- Adds CORS, startup/shutdown events
- TODO: Add background jobs (reminders, notifications), analytics
"""

from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import gigs, tenders, emergency, equipment, rides, users
from backend.models import User, Gig, Tender, EmergencyRequest
from backend.db import get_db
from backend.ai.matching import match_gig
from backend.ai.fraud import detect_fraud
from backend.ai.tender import analyze_tender
from backend.payments.mpesa import process_payment
# TODO: Add payments, admin routers when implemented

app = FastAPI(title="DigiKazi API")

# CORS setup
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(gigs.router)
app.include_router(tenders.router)
app.include_router(emergency.router)
app.include_router(equipment.router)
app.include_router(rides.router)
app.include_router(users.router)
# TODO: app.include_router(payments.router)
# TODO: app.include_router(admin.router)

@app.get("/")
def root():
    """Health check endpoint"""
    return {"message": "Welcome to DigiKazi API!"}

@app.post("/match-gig/")
def match_user_to_gig(user: User, db=Depends(get_db)):
    """
    Match a user to the best available gig using AI embeddings.
    """
    return match_gig(user, db)

@app.post("/analyze-tender/")
def analyze_tender_pdf(tender: Tender):
    """
    Analyze a tender PDF and extract key info.
    """
    return analyze_tender(tender.pdf_url)

@app.post("/emergency/")
def emergency_dispatch(request: EmergencyRequest, db=Depends(get_db)):
    """
    Handle emergency dispatch requests.
    """
    # ... logic to dispatch nearest responder ...
    return {"status": "dispatched", "location": request.location}

@app.post("/pay/")
def pay_with_mpesa(amount: float, phone: str):
    """
    Process M-Pesa payment.
    """
    return process_payment(amount, phone)

@app.on_event("startup")
async def startup_event():
    # TODO: Initialize DB, background jobs (reminders, notifications)
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # TODO: Clean up resources
    pass 