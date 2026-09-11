import os
import random
from datetime import datetime
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

async def start(update, context):
    await update.message.reply_text("Bienvenue LUCKY DJET 225 - tape /signal")

async def signal(update, context):
    c = round(random.uniform(1.2, 5.5), 2)
    h = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"SIGNAL: x{c} a {h}")

async def aide(update, context):
    await update.message.reply_text("Commandes: /start /signal /aide")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("aide", aide))
    app.run_polling()

if __name__ == "__main__":
    main()
