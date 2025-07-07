"""
WhatsApp Bot Integration (Twilio)
- Handles incoming/outgoing WhatsApp messages
- TODO: Implement user flows, language support, trust/safety prompts

Note: Requires Flask and Twilio Python packages. Install with:
    pip install flask twilio

Linter note: Import errors for Flask and Twilio are expected if not installed locally. Ignore if not running the bot locally.
"""

try:
    from flask import Flask, request  # Requires 'flask' package
    from twilio.twiml.messaging_response import MessagingResponse  # Requires 'twilio' package
except ImportError as e:
    raise ImportError("Missing required package. Please install Flask and Twilio with 'pip install flask twilio'.") from e
# from .flows import handle_message  # Uncomment and implement flows.py for real logic

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    """
    Webhook endpoint for incoming WhatsApp messages via Twilio.
    Parses the message and routes to the appropriate handler.
    """
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()
    # reply = handle_message(incoming_msg)  # Uncomment when flows.py is ready
    reply = "[Stub] Received: {}".format(incoming_msg)  # Placeholder reply
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    # Run the Flask app on port 5002 for local development
    app.run(port=5002)

# TODO: Set up Twilio webhook, parse messages, route to backend
# TODO: Add onboarding, gig matching, emergency, equipment, ride flows 