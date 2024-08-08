# inventory_manager.py
import sqlite3
from datetime import datetime, timedelta

# Function to add an item to the inventory
def add_item(item_name, quantity, location, expiration_date):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("INSERT INTO inventory (item_name, quantity, location, expiration_date) VALUES (?, ?, ?, ?)",
              (item_name, quantity, location, expiration_date))
    conn.commit()
    conn.close()

# Function to update an item's quantity in the inventory
def update_quantity(item_name, quantity):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("UPDATE inventory SET quantity = ? WHERE item_name = ?", (quantity, item_name))
    conn.commit()
    conn.close()

# Function to delete an item from the inventory
def delete_item(item_name):
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("DELETE FROM inventory WHERE item_name = ?", (item_name,))
    conn.commit()
    conn.close()

# Function to check the inventory for low stock, soon-to-expire, or expired items
def check_inventory():
    conn = sqlite3.connect('inventory.db')
    c = conn.cursor()
    c.execute("SELECT item_name, quantity, expiration_date FROM inventory")
    items = c.fetchall()
    
    low_stock = []
    soon_to_expire = []
    expired = []
    
    current_date = datetime.now()
    warning_period = timedelta(days=30)  # Warning period for soon-to-expire items
    
    for item in items:
        item_name, quantity, expiration_date = item
        if quantity < 5:  # Low stock threshold
            low_stock.append(item_name)
        
        if expiration_date:
            exp_date = datetime.strptime(expiration_date, "%Y-%m-%d")
            if exp_date < current_date:
                expired.append(item_name)
            elif exp_date < current_date + warning_period:
                soon_to_expire.append(item_name)
    
    conn.close()
    
    return low_stock, soon_to_expire, expired
