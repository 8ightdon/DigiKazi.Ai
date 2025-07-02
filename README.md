# 🚨 DigiKazi AI-Bot  
*"One WhatsApp bot for ALL hustles – from fundis to tenders to transport!"*  

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)  
[![Built for Kenyans](https://img.shields.io/badge/Made%20for-Kenya-FFD700)](https://vibehackathon.com)  



## 🚀 What is DigiKazi?

DigiKazi AI-Bot is an AI-powered WhatsApp bot that solves **5 critical problems** for Kenyan hustlers: emergencies, gigs, equipment, tenders, and transport. One chat, endless opportunities.

---

## 🌟 Expanded Features  
| Feature                | Tech Used          | Monetization                          |  
|------------------------|--------------------|---------------------------------------|  
| **Emergency Dispatch** | OpenAI + GPS       | KES 100/urgent job (+20% fee)         |  
| **Equipment Booking**  | Supabase GeoQuery  | 10% rental commission                 |  
| **Tender Alerts**      | NLP (PDF scraping) | KES 200/week for early bids           |  
| **Ride/Rider Matching**| Twilio Location    | KES 20/ride                           |  
| **Freelancer Matching**| OpenAI Embeddings  | KES 50–200/week listings              |  

---

## 🛠️ Unified Tech Stack  
**Core Stack:**  
- **Frontend**: WhatsApp (Twilio) + Streamlit admin dash  
- **Backend**: FastAPI + Supabase (PostgreSQL)  
- **AI**: OpenAI (NLP + embeddings), Hugging Face (fraud detection)  
- **Payments**: M-Pesa Daraja API  

**New Additions:**  
- **Equipment Tracking**: QR codes for tool check-in/out  
- **Tender Scraping**: BeautifulSoup for county websites  
- **Ride Matching**: Google Maps API for distance pricing  

---

## 👥 Dream Team & Roles  
| Role                  | Member       | Key Responsibilities                          | Superpower                          |  
|-----------------------|--------------|-----------------------------------------------|-------------------------------------|  
| **AI Architect**      | [Name]       | NLP matching, fraud detection, OpenAI/Supabase| Makes AI understand Sheng slang      |  
| **WhatsApp Maestro**  | [Name]       | Twilio flows, UX writing, demo recordings     | Gets 200+ WhatsApp replies/hour     |  
| **Backend Ninja**     | [Name]       | FastAPI, M-Pesa, database design              | Debugs while sleeping               |  
| **Data Scraper**      | [Name]       | Tender PDF parsing, equipment geo-tracking    | Extracts data from ANY website      |  
| **Pitch Commander**   | [Name]       | Investor slides, revenue models, storytelling | Turns bugs into "features"          |  

**How We Collaborate:**  
- **Morning Huddle**: 15-min Zoom to block blockers  
- **Slack Channels**: `#ai-wizards`, `#payment-warriors`, `#demo-or-die`  
- **Git Protocol**: PRs require 1 review + meme approval  

---

## 📜 License (MIT + Kenyan Compliance)  
```plaintext
Copyright (c) 2025 DigiKazi Team

Key Terms:
1. Requires attribution: "Powered by DigiKazi"
2. Complies with Kenya Data Protection Act (2019)
3. Bans use for illegal gigs (e.g., unlicensed transport)
```

---

## 🗂️ Planned Project Structure

```
backend/                # FastAPI backend, Supabase integration, API modules
  ├── main.py           # FastAPI app entrypoint
  ├── db.py             # Supabase/Postgres connection
  ├── models.py         # Pydantic models
  ├── routers/          # API route modules (gigs, tenders, emergency, etc.)
  ├── ai/               # AI models, embeddings, fraud detection
  ├── scraping/         # Scrapers for tenders, equipment, etc.
  ├── qr/               # QR code generation and logging
  └── utils/            # Helper functions
bot/                    # WhatsApp (Twilio) bot integration
  └── bot.py            # Main bot logic
streamlit_dashboard/    # Streamlit admin dashboard
  └── app.py            # Dashboard entrypoint
config/                 # Config files, secrets (env, etc.)
requirements.txt        # Python dependencies
.github/workflows/      # CI/CD workflows (GitHub Actions)
```

**Each module will include comments and TODOs for features like trust/safety, reminders, analytics, and language support.**