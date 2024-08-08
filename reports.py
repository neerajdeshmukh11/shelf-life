# reports.py
import sqlite3

def generate_report():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT * FROM inventory")
    items = c.fetchall()
    
    print("Current Inventory Report:")
    print("ID | Item Name | Quantity | Location | Expiration Date")
    for item in items:
        print(f"{item[0]} | {item[1]} | {item[2]} | {item[3]} | {item[4]}")
    
    conn.close()

if __name__ == "__main__":
    generate_report()
