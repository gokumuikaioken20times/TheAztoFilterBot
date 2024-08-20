# Telegram Bot

This is a Telegram bot that supports various commands like cloning, indexing, filtering, and more. Below are the details of how to set it up and use it.

## Setup

1. Clone the repository
2. Install dependencies using `pip install -r requirements.txt`
3. Create a `.env` file in the root directory to add your API keys and configurations:
    ```
    BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
    DATABASE_URL=YOUR_DATABASE_URL
    IMDB_API_KEY=YOUR_IMDB_API_KEY
    ```

4. Run the bot using `python main.py`

## Commands

- `/start`: Start the bot
- `/clone`: Create your own clone auto-filter bot
- `/index`: Index file from your channel
- `/logs`: Get recent errors
- ...
