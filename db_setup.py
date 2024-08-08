# db_setup.py
import sqlite3

def setup_database():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()

    # Create inventory table
    c.execute('''CREATE TABLE IF NOT EXISTS inventory
                 (id INTEGER PRIMARY KEY,
                  item_name TEXT,
                  quantity INTEGER,
                  location TEXT,
                  expiration_date TEXT)''')

    conn.commit()
    conn.close()

if __name__ == "__main__":
    setup_database()
    print("Database setup complete.")
