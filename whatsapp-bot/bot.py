# WhatsApp bot using Twilio
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
from whatsapp_bot.flows import handle_message

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_webhook():
    incoming_msg = request.values.get("Body", "").strip()
    resp = MessagingResponse()
    reply = handle_message(incoming_msg)
    resp.message(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(port=5002) 