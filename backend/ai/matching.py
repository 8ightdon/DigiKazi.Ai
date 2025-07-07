"""
AI Matching Module
- Handles user-to-gig/tender matching using embeddings and prompts
- TODO: Integrate OpenAI embeddings, prompt templates, and Supabase vector search
"""

# TODO: Implement match_user_to_gig(user, gig) using OpenAI embeddings
# TODO: Add prompt templates for matching

"""
AI logic for matching users to gigs using embeddings or simple keyword matching.
"""

def match_gig(user, db):
    """
    Matches a user to the best available gigs.
    Args:
        user (User): The user object containing skills, location, etc.
        db: Database connection or context (not used in stub).
    Returns:
        dict: Dictionary with a list of matched gigs (stubbed for demo).
    """
    # TODO: Replace with real embedding-based search using OpenAI/Supabase
    # For now, return a stubbed gig list
    return {
        "gigs": [
            {
                "id": "g1",
                "title": "Plumbing Job in Nairobi",
                "pay": 1500,
                "location": "Nairobi",
                "match_score": 0.95
            },
            {
                "id": "g2",
                "title": "Electrician Needed in Westlands",
                "pay": 2000,
                "location": "Nairobi",
                "match_score": 0.89
            }
        ],
        "message": "Matched gigs based on your skills and location (stub)."
    }
