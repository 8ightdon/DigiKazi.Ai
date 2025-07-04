"""
AI Matching Module
- Handles user-to-gig/tender matching using embeddings and prompts
- TODO: Integrate OpenAI embeddings, prompt templates, and Supabase vector search
"""

# TODO: Implement match_user_to_gig(user, gig) using OpenAI embeddings
# TODO: Add prompt templates for matching 

# AI logic for matching users to gigs
def match_gig(user, db):
    """
    Use OpenAI embeddings to match user to best gig.
    """
    # 1. Fetch gigs from DB
    gigs = db.table("gigs").select("*").execute().data
    # 2. Compute embedding similarity (pseudo-code)
    # 3. Return top match
    return {"matched_gig": gigs[0] if gigs else None} 