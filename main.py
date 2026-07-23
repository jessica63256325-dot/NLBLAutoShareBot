import asyncio
from telegram import Bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler

BOT_TOKEN = "8712541872:AAGTYTGoqEoL07weB2zBEzBIo2R1mcQzmiA"

GROUP_ID = -1004347995330

MESSAGE = """
📢 Please Share Our Group ❤️

🔗 https://t.me/+YdrtuYEDbVgyNjE1
"""

bot = Bot(BOT_TOKEN)

async def send_message():
    await bot.send_message(chat_id=GROUP_ID, text=MESSAGE)

async def main():
    scheduler = AsyncIOScheduler()
    scheduler.add_job(send_message, "interval", minutes=30)
    scheduler.start()

    print("Bot Started")

    await send_message()

    while True:
        await asyncio.sleep(3600)

asyncio.run(main())
