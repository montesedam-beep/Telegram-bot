from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, ChatMemberHandler
import os

WELCOME_MESSAGE = """🌈 Bienvenid@ a nuestro espacio seguro 💖✨
Aquí puedes conocer gente, compartir y ser tú mism@.
Respeto y cariño siempre 💕
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hola 👋, soy el bot de bienvenida. ¡Encantad@ de verte aquí!")

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.chat_member.new_chat_member:
        await context.bot.send_message(
            chat_id=update.chat_member.chat.id,
            text=WELCOME_MESSAGE
        )

def main():
    TOKEN = os.getenv("BOT_TOKEN")
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))

    print("Bot iniciado 🚀")
    app.run_polling()

if __name__ == "__main__":
    main()
