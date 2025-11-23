import sys # Import all required functions
from inventory_manager import view_inventory, add_item, update_item, delete_item

def display_menu():
    print("\n--- Grocery Store Management System ---")
    print("1. View Inventory")
    print("2. Add New Item")
    print("3. Update Item Stock/Price")
    print("4. Delete Item")
    print("5. Exit")
    print("---------------------------------------")

def run_system():
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            view_inventory()
        elif choice == '2':
            add_item()
        elif choice == '3':
            update_item()
        elif choice == '4':
            delete_item()
        elif choice == '5':
            print("\nExiting system. Goodbye! 👋")
            sys.exit()
        else:
            print("\n Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":

    run_system()# calling the function
