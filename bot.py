import os
import threading
from flask import Flask
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

BOT_TOKEN = os.environ.get("BOT_TOKEN")
app_flask = Flask(__name__)

@app_flask.route('/')
def home():
    return "Lucky Djet 225 - Bot en ligne!"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎰 Bienvenue sur Lucky Djet 225 !\n\nTape /jeu pour commencer le jeu !")

async def jeu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("✈️ Le jeu arrive bientôt ! Prépare tes mises !")

def run_flask():
    port = int(os.environ.get("PORT", 10000))
    app_flask.run(host="0.0.0.0", port=port)

def main():
    if not BOT_TOKEN:
        print("ERREUR: BOT_TOKEN manquant dans Render Environment!")
        return
    threading.Thread(target=run_flask, daemon=True).start()
    print("Bot Telegram démarré...")
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("jeu", jeu))
    application.run_polling()

if __name__ == "__main__":
    main()
