def get_flow_message(intent: str) -> str:
    """Returns a response message for each intent."""
    if intent == "emergency":
        return (
            "🚨 *Emergency Dispatch*\n\n"
            "Please send your location (e.g., 'South B') and the emergency type (e.g., 'fire', 'accident').\n"
            "We’ll dispatch the nearest responders after M-Pesa payment of KES 100."
        )
    elif intent == "tenders":
        return (
            "📑 *Tender Alerts*\n\n"
            "Reply with:\n"
            "1. Your county (e.g., 'Nairobi')\n"
            "2. Category (e.g., 'construction')\n"
            "3. Your budget range (optional)\n"
            "We’ll notify you when matching tenders are found!"
        )
    elif intent == "equipment":
        return (
            "🛠 *Equipment Booking*\n\n"
            "Send us:\n"
            "- Equipment type (e.g., concrete mixer)\n"
            "- Dates needed\n"
            "- Your location\n"
            "We’ll find and book the nearest available option for you."
        )
    elif intent == "transport":
        return (
            "🚗 *Ride / Rider Matching*\n\n"
            "Please reply with:\n"
            "- 'Need a ride' or 'Offering ride'\n"
            "- Pickup & destination\n"
            "- Preferred time\n"
            "We'll match you ASAP."
        )
    elif intent == "freelance":
        return (
            "💼 *Freelancer Hub*\n\n"
            "Reply with the service you need (e.g., plumber, graphic designer).\n"
            "We'll recommend top-rated hustlers near you."
        )
    else:
        return (
            "❓ Sorry, I didn’t get that. Please type a number from the menu."
        )
