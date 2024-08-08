# alerts.py
from inventory_manager import check_inventory

def send_alerts():
    low_stock, soon_to_expire, expired = check_inventory()
    
    if low_stock:
        print("Low stock alert for the following items:")
        for item in low_stock:
            print(f"- {item}")
    
    if soon_to_expire:
        print("Soon-to-expire items alert for the following items:")
        for item in soon_to_expire:
            print(f"- {item} (expires soon)")
    
    if expired:
        print("Expired items alert for the following items:")
        for item in expired:
            print(f"- {item} (expired)")

if __name__ == "__main__":
    send_alerts()
