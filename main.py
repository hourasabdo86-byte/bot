import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("أهلا يا عبده! البوت شغال تمام ✅")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"انت قولت: {update.message.text}")

def main():
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("حط التوكن في متغير اسمه BOT_TOKEN")
        return
    app = ApplicationBuilder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
