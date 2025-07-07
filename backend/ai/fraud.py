"""
AI logic for detecting fraud in job/tender messages using keywords or ML models.
"""

def detect_fraud(text: str):
    """
    Detects potential fraud in a given text using simple keyword matching.
    Args:
        text (str): The message or job description to analyze.
    Returns:
        dict: Fraud detection result (stubbed for demo).
    """
    # TODO: Replace with real ML model or Hugging Face classifier
    # Simple keyword-based detection for demo
    fraud_keywords = ["advance fee", "send money", "urgent payment", "scam"]
    found = [kw for kw in fraud_keywords if kw in text.lower()]
    if found:
        return {
            "fraud": True,
            "reasons": found,
            "message": "Potential fraud detected (stub)."
        }
    else:
        return {
            "fraud": False,
            "reasons": [],
            "message": "No fraud detected (stub)."
        } 