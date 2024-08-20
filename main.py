from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from config.config import BOT_TOKEN
from handlers.commands import start, clone, index, logs
from handlers.filters import filter, filters
from handlers.admin import ban, unban

def main():
    updater = Updater(BOT_TOKEN)
    dispatcher = updater.dispatcher

    # Command handlers
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("clone", clone))
    dispatcher.add_handler(CommandHandler("index", index))
    dispatcher.add_handler(CommandHandler("logs", logs))
    dispatcher.add_handler(CommandHandler("filter", filter))
    dispatcher.add_handler(CommandHandler("filters", filters))
    dispatcher.add_handler(CommandHandler("ban", ban))
    dispatcher.add_handler(CommandHandler("unban", unban))
    
    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
