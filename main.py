import os
import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = os.environ["BOT_TOKEN"]

GROUP_ID = -1004347995330

MESSAGE = """
📢 Please Share Our Group ❤️

🔗 https://t.me/+YdrtuYEDbVgyNjE1
"""

bot = Bot(BOT_TOKEN)

async def send_message():
    await bot.send_message(
        chat_id=GROUP_ID,
        text=MESSAGE
    )

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message, "interval", minutes=30)
    scheduler.start()

    print("Bot Started")

    await send_message()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())
