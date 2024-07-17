import sqlite3

class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
    
    def save_to_db(self):
        conn = sqlite3.connect("database.db")
        db = conn.cursor()
        db.execute("INSERT INTO customers (name, phone) VALUES (?, ?)", (self.name, self.phone))
        conn.commit()
        conn.close()

    @staticmethod   # function that belongs to class, not just instance of class
    def get_customer_id(phone):
        conn = sqlite3.connect("database.db")
        db = conn.cursor()
        db.execute("SELECT id FROM customers WHERE phone = ?", (phone,))
        result = db.fetchone()
        conn.close()
        return result[0] if result else None


class Order:
    def __init__(self, customer_id, items, total_price):
        self.customer_id = customer_id
        self.items = items
        self.total_price = total_price

    def save_to_db(self):
        conn = sqlite3.connect("database.db")
        db = conn.cursor()
        db.execute("INSERT INTO orders (customer_id, items, total_price) VALUES (?, ?, ?)", (self.customer_id, self.items, self.total_price))
        conn.commit()
        conn.close()
    