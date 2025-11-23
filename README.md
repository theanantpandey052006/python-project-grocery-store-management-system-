# python-project-grocery-store-management-system-
## Overview of the Project
The project is designed to allow a small store owner or inventory manager to efficiently track stock levels and pricing, which addresses the objective of applying course concepts in a real-world context.
## Project Title 
The Grocery Store Inventory Management System (GSIMS) is a simple, console-based application designed to help small businesses efficiently manage their product inventory. It utilizes a modular Python structure to perform core CRUD (Create, Read, Update, Delete) operations on inventory data, ensuring accuracy in stock levels and pricing.
The system is broken down into three logical modules to demonstrate modular and clean implementation and the proper architectural design.
## Features
The GSIMS provides the following key features:
View Inventory: Displays a neatly formatted table showing all items, their current stock quantity, and unit price. (Implemented in inventory_ui.py and inventory_data.py).
Add New Item: Allows a user to introduce new products into the inventory with initial stock and price. Includes input validation. (Implemented in inventory_ui.py and inventory_data.py).
Update Item: Allows the user to modify the stock quantity and/or the unit price of an existing item. Includes input validation. (Implemented in inventory_ui.py and inventory_data.py).
Delete Item: Removes an item entirely from the inventory list. (Implemented in inventory_ui.py and inventory_data.py).
Logical Workflow: A persistent main menu ensures a clear and easy-to-use user interaction flow.
## Technologies/Tools Used
Python 3.x
Dictionaries
GitHub
## Instructions for Testing 
Since this is a console application, testing primarily involves manual validation of all functional paths:
Test 1: View Inventory (Option 1)
Action: Select option 1.
Expected Result: A clean, formatted table showing Apples, Bananas, and Milk and their initial quantities/prices.
Test 2: Add New Item (Option 2) - Positive Case
Action: Select option 2. Enter sugar, quantity 100, price 1.25.
Expected Result: "Sugar added successfully." Run Option 1 again to confirm Sugar is listed.
Test 3: Update Item (Option 3) - Validation/Error Handling
Action: Select option 3. Enter milk. Enter new quantity -5 (or any non-number).
Expected Result: "Invalid input. Check if quantity is a whole number and price is a positive number." 
Test 4: Delete Item (Option 4)
Action: Select option 4. Enter bananas.
Expected Result: "Bananas deleted successfully." Run Option 1 to confirm Bananas is removed.
Test 5: Exit (Option 5)
Action: Select option 5.
Expected Result: "Exiting system. Goodbye! 👋" and the program terminates.
## Screenshot of result
<img width="362" height="220" alt="image" src="https://github.com/user-attachments/assets/bd143180-1c1d-4bfc-8b60-075269f53b62" />

