import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from dotenv import load_dotenv
from subprocess import check_output

load_dotenv()

TOKEN = os.getenv("TELEGRAM_TOKEN")

def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text("Hello! Send me a message to receive a response from the model!")

def handle_message(update: Update, context: CallbackContext) -> None:
    user_message = update.message.text
    response = check_output(["python", "model.py", user_message]).decode("utf-8")
    update.message.reply_text(response)

def main():
    updater = Updater(TOKEN)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
