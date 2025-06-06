from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    data = request.json
    msg = data.get("message", "No message received.")
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }
    requests.post(url, json=payload, timeout=3)
    return "Message sent to Telegram", 200

@app.route("/", methods=["GET"])
def home():
    return "✅ Bot is live. Use POST to send signal.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
