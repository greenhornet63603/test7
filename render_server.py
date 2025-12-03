import threading
import asyncio
from flask import Flask
import main

app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running on Render!"

def start_bot():
    asyncio.run(main.main())

if __name__ == "__main__":
    # Start bot in background
    bot_thread = threading.Thread(target=start_bot)
    bot_thread.start()

    # Start web server for Render always on
    app.run(host="0.0.0.0", port=10000)
