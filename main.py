from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    try:
        msg = ""
        if request.is_json:
            data = request.get_json()
            msg = data.get("message", "No message received.")
        else:
            msg = request.data.decode("utf-8") or "No message received."

        requests.post(
            f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage",
            json={"chat_id": CHAT_ID, "text": msg},
            timeout=3
        )
        return "Message sent", 200
    except Exception as e:
        return f"Error: {e}", 500
