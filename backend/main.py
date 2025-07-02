"""
DigiKazi AI-Bot Backend Entrypoint (Unified & Modular)
- Imports and includes all routers
- Adds CORS, startup/shutdown events
- TODO: Add background jobs (reminders, notifications), analytics
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routers import gigs, tenders, emergency, equipment, rides, users
# TODO: Add payments, admin routers when implemented

app = FastAPI(title="DigiKazi AI-Bot API")

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
    return {"message": "DigiKazi AI-Bot backend is running!"}

@app.on_event("startup")
async def startup_event():
    # TODO: Initialize DB, background jobs (reminders, notifications)
    pass

@app.on_event("shutdown")
async def shutdown_event():
    # TODO: Clean up resources
    pass 