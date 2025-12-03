from flask import Flask
import threading
import asyncio
import main

app = Flask(__name__)

@app.route("/")
def home():
    return "Test7 Bot Running on Render!"

def start_bot():
    try:
        asyncio.run(main.main())
    except RuntimeError:
        loop = asyncio.get_event_loop()
        loop.create_task(main.main())

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()

    import os
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)
