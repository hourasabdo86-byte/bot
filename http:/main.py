import os
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("البوت شغال يا عبده! ✅")

def main():
    token = os.environ.get("BOT_TOKEN")
    app = Application.builder().token(token).build()
    app.add_handler(CommandHandler("start", start))
    print("Bot started...")
    app.run_polling()

if __name__ == "__main__":
    main()
