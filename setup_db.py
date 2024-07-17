import sqlite3

def initalize_db():
    conn = sqlite3.connect("database.db")
    db = conn.cursor()

    db.execute('''CREATE TABLE IF NOT EXISTS customers (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name TEXT NOT NULL,
                        phone TEXT NOT NULL UNIQUE)''')
    
    db.execute('''CREATE TABLE IF NOT EXISTS orders (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        customer_id INTEGER,
                        items TEXT NOT NULL,
                        total_price REAL NOT NULL,
                        FOREIGN KEY (customer_id) REFERENCES customers(id))''')
    
    conn.commit()
    conn.close()