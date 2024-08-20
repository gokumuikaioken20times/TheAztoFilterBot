import logging
from config.config import LOG_FILE

logging.basicConfig(filename=LOG_FILE, level=logging.INFO)

def log_action(update, action):
    logging.info(f"User {update.effective_user.id} executed {action}.")
