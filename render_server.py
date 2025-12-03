from flask import Flask
import threading
import main  # your bot starts here

app = Flask(__name__)

@app.route("/")
def home():
    return "Test7 Bot Running on Render!"

def start_bot():
    main  # importing main auto-starts bot

if __name__ == "__main__":
    threading.Thread(target=start_bot).start()

    import os
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
