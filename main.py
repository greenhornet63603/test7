import asyncio
from pyrogram import Client
from config import Config

# Create client (use YOUR API_ID, API_HASH, BOT_TOKEN from Config)
stark = Client(
    "stark",
    api_id=Config.API_ID,
    api_hash=Config.API_HASH,
    bot_token=Config.BOT_TOKEN,
)

# Import handlers (your __init__.py handlers)
import __init__  # IMPORTANT: keeps your handlers active


async def main():
    print("Starting bot...")
    await stark.start()
    print("Bot is running!")
    await asyncio.Event().wait()  # keeps bot running forever


if __name__ == "__main__":
    asyncio.run(main())
