"""
Message handling logic for DigiKazi WhatsApp Bot.
Routes user messages to the appropriate feature flow.
"""

def handle_message(msg):
    """
    Main entry point for processing incoming WhatsApp messages.
    Args:
        msg (str): The incoming message text from the user.
    Returns:
        str: The reply to send back to the user.
    """
    # Normalize message to lowercase for easier matching
    msg_lower = msg.lower()

    # Emergency flow: If user mentions 'emergency', trigger emergency response
    if "emergency" in msg_lower:
        return "🚨 Emergency received! Please share your location."
    # Gig flow: If user asks for gigs, provide latest gigs
    elif "gig" in msg_lower:
        return "🛠️ Here are the latest gigs for you... (feature coming soon)"
    # Tender flow: If user asks for tenders, provide tender alerts
    elif "tender" in msg_lower:
        return "📄 Fetching latest tenders. Please wait... (feature coming soon)"
    # Equipment flow: If user asks about equipment, start booking process
    elif "equipment" in msg_lower:
        return "🔧 Equipment booking: Please specify what you need. (feature coming soon)"
    # Ride flow: If user asks for a ride, start ride matching
    elif "ride" in msg_lower:
        return "🛵 Ride request received! Please share your pickup location. (feature coming soon)"
    # Default: Welcome/help message
    else:
        return (
            "👋 Welcome to DigiKazi!\n"
            "Type 'gig', 'tender', 'emergency', 'equipment', or 'ride' to get started.\n"
            "For help, type 'help'."
        )
