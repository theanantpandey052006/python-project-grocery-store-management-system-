# inventory_manager.py
from inventory_data import INVENTORY

def view_inventory():
    """Prints the current inventory."""
    if not INVENTORY:
        print("\nThe inventory is empty.")
        return
        
    print("\n--- Current Inventory ---")
    print(f"{'Item Name':<15} {'Stock':<10} {'Price ($)':<10}")
    print("-" * 35)
    
    for item, details in INVENTORY.items():
        quantity, price = details
        print(f"{item.capitalize():<15} {quantity:<10} {price:<10.2f}")

def add_item():
    """Adds a new item to the inventory."""
    name = input("Enter item name to add: ").lower()
    if name in INVENTORY:
        print(f"Error: {name.capitalize()} already exists. Use 'Update' to modify.")
        return

    try:
        quantity = int(input("Enter initial stock quantity: "))
        price = float(input("Enter price per unit ($): "))
        if quantity < 0 or price < 0:
            raise ValueError
        
        INVENTORY[name] = [quantity, price]
        print(f"\n {name.capitalize()} added successfully.")
    except ValueError:
        print("\n Invalid input. Quantity must be a whole number, and price must be a positive number.")

def update_item():
    """Updates the stock or price of an existing item."""
    name = input("Enter item name to update: ").lower()
    
    if name not in INVENTORY:
        print(f"Error: {name.capitalize()} not found in inventory.")
        return

    print(f"\nUpdating {name.capitalize()} - Current Stock: {INVENTORY[name][0]}, Current Price: ${INVENTORY[name][1]:.2f}")
    
    try:
        new_quantity = input("Enter new stock quantity (leave blank to keep current): ")
        new_price = input("Enter new price ($) (leave blank to keep current): ")

        if new_quantity:
            new_quantity = int(new_quantity)
            if new_quantity < 0: raise ValueError
            INVENTORY[name][0] = new_quantity
            
        if new_price:
            new_price = float(new_price)
            if new_price < 0: raise ValueError
            INVENTORY[name][1] = new_price
            
        print(f"\n {name.capitalize()} updated successfully.")
        
    except ValueError:
        print("\n Invalid input. Check if quantity is a whole number and price is a positive number.")

def delete_item():
    """Deletes an item from the inventory."""
    name = input("Enter item name to delete: ").lower()
    
    if name in INVENTORY:
        del INVENTORY[name]
        print(f"\n {name.capitalize()} deleted successfully.")
    else:

        print(f"Error: {name.capitalize()} not found in inventory.")

