from telegram import Update
from telegram.ext import CallbackContext
from utils.database import add_filter, get_filters

def filter(update: Update, context: CallbackContext):
    filter_text = " ".join(context.args)
    if filter_text:
        add_filter(filter_text)
        update.message.reply_text(f"Filter '{filter_text}' added.")
    else:
        update.message.reply_text("Please provide filter text.")

def filters(update: Update, context: CallbackContext):
    all_filters = get_filters()
    update.message.reply_text("\n".join(all_filters))
