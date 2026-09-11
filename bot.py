import os
import random
import threading
from datetime import datetime
from flask import Flask
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = os.getenv("BOT_TOKEN")

flask_app = Flask(__name__)

@flask_app.route('/')
def home():
    return "Bot Lucky Djet 225 en ligne ! 🚀"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bienvenue sur Lucky Djet 225 🇨🇮\nEnvoie /signal pour un pronostic ✈️")

async def signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    c = round(random.uniform(1.2, 5.5), 2)
    h = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"SIGNAL ✈️\nCote : {c}x\nHeure : {h}\nBonne chance !")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    
    threading.Thread(target=run_flask, daemon=True).start()
    print("Bot Telegram démarré...")
    app.run_polling()
