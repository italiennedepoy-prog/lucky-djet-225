import os
import logging
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

logging.basicConfig(level=logging.INFO)

# 1. Petit serveur pour Render
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot is Live")
    def log_message(self, format, *args):
        return

def run_web():
    port = int(os.environ.get("PORT", 10000))
    print(f"Starting web server on port {port}")
    HTTPServer(("0.0.0.0", port), H).serve_forever()

Thread(target=run_web, daemon=True).start()

# 2. Bot Telegram
TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    print("ERREUR: BOT_TOKEN manquant!")
    raise ValueError("BOT_TOKEN not set")

print("TOKEN found, starting bot...")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut ! Lucky Djet 225 🚀\nEnvoie /predire pour une prédiction")

async def predire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🎯 Prochain tour : x2.15\n💰 Ferme à x1.80 pour sécuriser !")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predire", predire))

print("Bot polling started...")
app.run_polling()
