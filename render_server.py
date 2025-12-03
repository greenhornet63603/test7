import threading
from flask import Flask
import asyncio
import main   # import your main.py file

# -----------------------
#  Start your bot/server
# -----------------------
def start_bot():
    asyncio.run(main.main())

# -----------------------
#  Dummy web server
# -----------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "Bot is running on Render!"

# -----------------------
#  Start both (bot + web)
# -----------------------
threading.Thread(target=start_bot).start()
