# main.py
from db_setup import setup_database
from inventory_manager import add_item, update_quantity, delete_item
from alerts import send_alerts
from reports import generate_report

def main():
    setup_database()

    while True:
        print("\nInventory Management System")
        print("1. Add Item")
        print("2. Update Quantity")
        print("3. Delete Item")
        print("4. Send Alerts")
        print("5. Generate Report")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            location = input("Enter location: ")
            expiration_date = input("Enter expiration date (YYYY-MM-DD): ")
            add_item(item_name, quantity, location, expiration_date)
        elif choice == '2':
            item_name = input("Enter item name: ")
            quantity = int(input("Enter new quantity: "))
            update_quantity(item_name, quantity)
        elif choice == '3':
            item_name = input("Enter item name to delete: ")
            delete_item(item_name)
        elif choice == '4':
            send_alerts()
        elif choice == '5':
            generate_report()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()
