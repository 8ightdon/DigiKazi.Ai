# Fraud detection logic
def detect_fraud(message: str):
    """
    Use Hugging Face model or keyword rules to detect fraud.
    """
    suspicious_keywords = ["mpesa refund", "urgent send", "lottery", "advance fee"]
    for word in suspicious_keywords:
        if word in message.lower():
            return {"fraud": True, "reason": f"Keyword detected: {word}"}
    return {"fraud": False} 