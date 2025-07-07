"""
Test for the gig matching AI logic in DigiKazi backend.
"""

# Import the match_gig function and User model from the backend
from backend.ai.matching import match_gig
from backend.models import User

# In a real test, you would use a mock or fixture for the database

def test_match_gig():
    """
    Test that the match_gig function returns a result containing 'gigs' for a sample user.
    """
    user = User(
        id="1",
        name="Test User",
        phone="0712345678",
        skills=["plumbing"],
        location="Nairobi",
        role="fundi"
    )
    db = None  # Replace with a mock or fixture in real tests
    result = match_gig(user, db)
    # Assert that the result contains the expected key (example logic)
    assert "gigs" in result 