import asyncio
from telegram import Bot

BOT_TOKEN = "8712541872:AAG9qHuLKGTSDkmK9AIcbXGfZU4Y8W5KxDg"
GROUP_ID = -1004347995330

MESSAGE = """
🔥 NL BL EXPOSED 🔥

✅ Join Now
https://is.gd/3MfYhX

Select age 26+ on my page ❤️

#Netherlands #Belgium
"""

async def main():
bot = Bot(token=BOT_TOKEN)
await bot.send_message(chat_id=GROUP_ID, text=MESSAGE)

asyncio.run(main())
