from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! رباتت روشنه ✅")

app = ApplicationBuilder().token("8493565596:AAFIHaWJ1v6L1b-KiTSPJGc9Z1dVr1KpvW4").build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
