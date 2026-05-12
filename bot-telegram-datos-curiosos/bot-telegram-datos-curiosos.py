from telegram import Update
from telegram.ext import CommandHandler, ApplicationBuilder, ContextTypes
import requests
from deep_translator import GoogleTranslator

TOKEN= "AQUI PONES EL TOKEN DE TU BOT DE TELEGRAM"


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola bienvenido a este mini app" \
    "\n/start\n/dato\n/tiempo + 'ciudad'")

async def dato(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Pulsa aquí para recibir mas datos curiosos:\n\n/dato\n\n---------------------------"
    "--------------------------------")
    url="https://uselessfacts.jsph.pl/random.json?language=es"

    response= requests.get(url)
    data=response.json()
    
    fact=data["text"]
    fact_es=GoogleTranslator(source="auto",target="es").translate(fact)
    await update.message.reply_text(f"📚Dato curioso:\n {fact_es}")




app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("dato",dato))

app.run_polling(allowed_updates=Update.ALL_TYPES)