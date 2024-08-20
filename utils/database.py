import sqlite3

conn = sqlite3.connect('bot.db')
c = conn.cursor()

def add_filter(filter_text):
    c.execute("INSERT INTO filters (filter_text) VALUES (?)", (filter_text,))
    conn.commit()

def get_filters():
    c.execute("SELECT filter_text FROM filters")
    return [row[0] for row in c.fetchall()]
