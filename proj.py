import nest_asyncio
import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, CallbackContext

# فعال‌سازی nest_asyncio برای اجازه دادن به حلقه رخداد‌های تو در تو
nest_asyncio.apply()

# تابعی برای شروع بات
async def start(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('سلام! من یک بات تلگرام هستم. چطور می‌توانم کمک کنم؟')

# تابعی برای پاسخ به پیام‌های کاربر
async def echo(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text(update.message.text)

# تابع اصلی برای راه‌اندازی بات
async def main() -> None:
    # توکن بات خود را اینجا وارد کنید
    application = ApplicationBuilder().token("7140363296:AAFyqCXSTvqjN6r9myIdBbQ2rRORnAz7Yzc").build()

    # هندلر برای دستور /start
    application.add_handler(CommandHandler("start", start))

    # هندلر برای پیام‌های متنی
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # راه‌اندازی بات
    await application.run_polling()


if __name__ == '__main__':
    asyncio.run(main())
