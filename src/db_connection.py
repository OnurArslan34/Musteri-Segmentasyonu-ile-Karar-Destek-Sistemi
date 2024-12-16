import sqlite3

def get_connection(db_path="data/products.db"):
    conn = sqlite3.connect(db_path)
    return conn
