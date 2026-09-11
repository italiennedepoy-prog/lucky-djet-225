import os
import random
import threading
from datetime import datetime
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler

TOKEN = os.getenv("BOT_TOKEN")

# Serveur Flask pour Render
flask_app = Flask(__name__)
@flask_app.route('/')
def home():
    return "Bot Lucky Djet 225 en ligne !"

async def start(update, context):
    await update.message.reply_text("Bienvenue sur Lucky Djet 225 ! Tape /signal pour un signal.")

async def signal(update, context):
    c = round(random.uniform(1.2, 5.5), 2)
    h = datetime.now().strftime("%H:%M:%S")
    await update.message.reply_text(f"SIGNAL\nCote: {c}x\nHeure: {h}")

async def aide(update, context):
    await update.message.reply_text("Commandes:\n/start - Demarrer\n/signal - Signal\n/aide - Aide")

def run_bot():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("signal", signal))
    app.add_handler(CommandHandler("aide", aide))
    app.run_polling()

if __name__ == "__main__":
    threading.Thread(target=run_bot).start()
    port = int(os.environ.get("PORT", 10000))
    flask_app.run(host="0.0.0.0", port=port)
