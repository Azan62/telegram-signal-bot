from flask import Flask, request
import requests
import os

app = Flask(__name__)

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")

@app.route("/", methods=["POST"])
def webhook():
    try:
        data = request.get_json(force=True)  # Robust JSON parsing
        msg = data.get("message", "⚠️ No message content provided.")
        
        # Log for debugging
        print("✅ Received from TradingView:", msg)

        # Send message to Telegram
        url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
        payload = {
            "chat_id": CHAT_ID,
            "text": msg
        }
        tg_response = requests.post(url, json=payload, timeout=5)

        # Debug response from Telegram
        print("📨 Telegram API response:", tg_response.status_code, tg_response.text)

        return "✅ Message sent to Telegram", 200
    except Exception as e:
        print("❌ Error:", e)
        return f"Error: {e}", 400

@app.route("/", methods=["GET"])
def home():
    return "✅ Bot is live. Use POST to send signal.", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
