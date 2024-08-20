from telegram import Update
from telegram.ext import CallbackContext

def ban(update: Update, context: CallbackContext):
    user_id = context.args[0]
    # Add code to ban user
    update.message.reply_text(f"User {user_id} has been banned.")

def unban(update: Update, context: CallbackContext):
    user_id = context.args[0]
    # Add code to unban user
    update.message.reply_text(f"User {user_id} has been unbanned.")
