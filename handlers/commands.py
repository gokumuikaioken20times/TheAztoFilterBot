from telegram import Update
from telegram.ext import CallbackContext
from utils.logger import log_action

def start(update: Update, context: CallbackContext):
    update.message.reply_text("Welcome to the bot!")
    log_action(update, "start")

def clone(update: Update, context: CallbackContext):
    update.message.reply_text("Cloning the bot...")
    log_action(update, "clone")

def index(update: Update, context: CallbackContext):
    update.message.reply_text("Indexing files...")
    log_action(update, "index")

def logs(update: Update, context: CallbackContext):
    update.message.reply_text("Fetching logs...")
    log_action(update, "logs")
