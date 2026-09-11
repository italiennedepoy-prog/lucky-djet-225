import os
from threading import Thread
from http.server import HTTPServer, BaseHTTPRequestHandler
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Petit serveur pour Render (gratuit)
class H(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Bot OK")

def web():
    p = int(os.environ.get("PORT", 10000))
    HTTPServer(("0.0.0.0", p), H).serve_forever()

Thread(target=web, daemon=True).start()

# Ton bot
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Salut ! Je suis Lucky Djet 225 🚀 Envoie /predire")

async def predire(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Prochain tour : x2.15 - Ferme à x1.80 pour sécuriser !")

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("predire", predire))
app.run_polling()
