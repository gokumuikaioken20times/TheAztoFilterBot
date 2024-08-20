import os

# Load sensitive data from environment variables or define them here
BOT_TOKEN = os.getenv("BOT_TOKEN")
DATABASE_URL = os.getenv("DATABASE_URL")
LOG_FILE = "bot.log"

# Other configurations
IMDB_API_KEY = os.getenv("IMDB_API_KEY")
