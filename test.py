class Member:
    def __init__(self, member_id, name, email):
        self.member_id = member_id
        self.name = name
        self.email = email

    def update_information(self, name, email):
        self.name = name
        self.email = email

class Item:
    def __init__(self, item_id, name, price, in_stock):
        self.item_id = item_id
        self.name = name
        self.price = price
        self.in_stock = in_stock
        self.categories = []  # Initialize an empty list for categories

    def update_stock_price(self, in_stock, price):
        self.in_stock = in_stock
        self.price = price

class Category:
    def __init__(self, name):
        self.name = name

    def add_item(self, item):
        item.categories.append(self)  # Update the item's categories list


class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def search_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def list_items_by_category(self, category_name):
        items_in_category = []
        for item in self.items:
            if category_name in [cat.name for cat in item.categories]:
                items_in_category.append(item)
        return items_in_category

class Transaction:
    def __init__(self, member, items):
        self.member = member
        self.items = items

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

    def calculate_total(self):
        total = sum(item.price for item in self.items)
        return total

# Sample usage #1
# if __name__ == "__main__":
#     # Create members
#     member1 = Member(1, "John Doe", "john@example.com")
#     member2 = Member(2, "Jane Smith", "jane@example.com")

#     # Create items
#     item1 = Item(101, "Product A", 10.99, 100)
#     item2 = Item(102, "Product B", 5.99, 50)

#     # Create categories
#     category1 = Category("Electronics")
#     category2 = Category("Clothing")

#     category1.add_item(item1)
#     category2.add_item(item2)

#     # Create inventory
#     inventory = Inventory()
#     inventory.add_item(item1)
#     inventory.add_item(item2)

#     # Create a transaction
#     transaction = Transaction(member1, [item1, item2])

#     # Perform actions based on user input
#     # You can implement a menu-driven interface here for adding/updating/removing members/items, processing transactions, etc.
#     # Use the defined classes and methods to interact with the data.

#     # Example: Updating member information
#     member1.update_information("New Name", "newemail@example.com")

#     # Example: Updating item information
#     item1.update_stock_price(90, 11.99)

#     # Example: Processing a transaction
#     total_spend = transaction.calculate_total()
#     print(f"Total spend in the transaction: ${total_spend}")

#     # Example: Searching for an item
#     item = inventory.search_item(101)
#     if item:
#         print(f"Item found: {item.name}")
#     else:
#         print("Item not found.")

#     # Example: Listing items by category
#     items_in_category = inventory.list_items_by_category("Electronics")
#     print("Items in Electronics category:")
#     for item in items_in_category:
#         print(f"{item.name} - {item.price}")

# Sample usage #2
# ... (previous code for classes)
# if __name__ == "__main__":
#     # Create some initial members, items, and categories
#     members = {}
#     items = {}
#     categories = {}
#     inventory = Inventory()
#     transactions = []

#     while True:
#         print("\nRetail Store Management Program")
#         print("1. Add Member")
#         print("2. Add Item")
#         print("3. Update Member Information")
#         print("4. Update Item Information")
#         print("5. Add Item to Category")
#         print("6. Remove Item from Category")
#         print("7. Process Transaction")
#         print("8. List Items by Category")
#         print("9. Exit")
#         choice = input("Enter your choice: ")

#         if choice == "1":
#             # Add Member
#             member_id = int(input("Enter Member ID: "))
#             name = input("Enter Member Name: ")
#             email = input("Enter Member Email: ")
#             member = Member(member_id, name, email)
#             members[member_id] = member

#         elif choice == "2":
#             # Add Item
#             item_id = int(input("Enter Item ID: "))
#             name = input("Enter Item Name: ")
#             price = float(input("Enter Item Price: "))
#             in_stock = int(input("Enter In-Stock Quantity: "))
#             item = Item(item_id, name, price, in_stock)
#             items[item_id] = item
#             inventory.add_item(item)

#         elif choice == "3":
#             # Update Member Information
#             member_id = int(input("Enter Member ID to update: "))
#             if member_id in members:
#                 name = input("Enter New Member Name: ")
#                 email = input("Enter New Member Email: ")
#                 members[member_id].update_information(name, email)
#             else:
#                 print("Member not found.")

#         elif choice == "4":
#             # Update Item Information
#             item_id = int(input("Enter Item ID to update: "))
#             if item_id in items:
#                 price = float(input("Enter New Item Price: "))
#                 in_stock = int(input("Enter New In-Stock Quantity: "))
#                 items[item_id].update_stock_price(in_stock, price)
#             else:
#                 print("Item not found.")

#         elif choice == "5":
#             # Add Item to Category
#             item_id = int(input("Enter Item ID: "))
#             category_name = input("Enter Category Name: ")
#             if item_id in items and category_name in categories:
#                 categories[category_name].add_item(items[item_id])
#             else:
#                 print("Item or Category not found.")

#         elif choice == "6":
#             # Remove Item from Category
#             item_id = int(input("Enter Item ID: "))
#             category_name = input("Enter Category Name: ")
#             if item_id in items and category_name in categories:
#                 items[item_id].categories.remove(categories[category_name])
#             else:
#                 print("Item or Category not found.")

#         elif choice == "7":
#             # Process Transaction
#             member_id = int(input("Enter Member ID: "))
#             if member_id in members:
#                 transaction_items = []
#                 while True:
#                     item_id = int(input("Enter Item ID to add to the transaction (0 to finish): "))
#                     if item_id == 0:
#                         break
#                     if item_id in items:
#                         transaction_items.append(items[item_id])
#                     else:
#                         print("Item not found.")
#                 if transaction_items:
#                     transaction = Transaction(members[member_id], transaction_items)
#                     transactions.append(transaction)
#                     total_spend = transaction.calculate_total()
#                     print(f"Total spend in the transaction: ${total_spend}")
#                 else:
#                     print("No items in the transaction.")
#             else:
#                 print("Member not found.")

#         elif choice == "8":
#             # List Items by Category
#             category_name = input("Enter Category Name: ")
#             if category_name in categories:
#                 items_in_category = inventory.list_items_by_category(category_name)
#                 print(f"Items in {category_name} category:")
#                 for item in items_in_category:
#                     print(f"{item.name} - Price: ${item.price}, In-Stock: {item.in_stock}")
#             else:
#                 print("Category not found.")

#         elif choice == "9":
#             print("Exiting the program. Goodbye!")
#             break

#         else:
#             print("Invalid choice. Please select a valid option.")

# With Error Handling
# ... (previous code for classes)

# Sample usage
if __name__ == "__main__":
    # Create some initial members, items, and categories
    members = {}
    items = {}
    categories = {}
    inventory = Inventory()
    transactions = []

    while True:
        print("\nRetail Store Management Program")
        print("1. Add Member")
        print("2. Add Item")
        print("3. Update Member Information")
        print("4. Update Item Information")
        print("5. Add Item to Category")
        print("6. Remove Item from Category")
        print("7. Process Transaction")
        print("8. List Items by Category")
        print("9. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            # Add Member
            try:
                member_id = int(input("Enter Member ID: "))
                if member_id in members:
                    print("Member ID already exists.")
                else:
                    name = input("Enter Member Name: ")
                    email = input("Enter Member Email: ")
                    member = Member(member_id, name, email)
                    members[member_id] = member
                    print("Member added successfully.")
            except ValueError:
                print("Invalid input for Member ID. Please enter a number.")

        elif choice == "2":
            # Add Item
            try:
                item_id = int(input("Enter Item ID: "))
                if item_id in items:
                    print("Item ID already exists.")
                else:
                    name = input("Enter Item Name: ")
                    price = float(input("Enter Item Price: "))
                    in_stock = int(input("Enter In-Stock Quantity: "))
                    item = Item(item_id, name, price, in_stock)
                    items[item_id] = item
                    inventory.add_item(item)
                    print("Item added successfully.")
            except ValueError:
                print("Invalid input for Item ID, Price, or In-Stock. Please enter valid numbers.")

        elif choice == "3":
            # Update Member Information
            try:
                member_id = int(input("Enter Member ID to update: "))
                if member_id in members:
                    name = input("Enter New Member Name: ")
                    email = input("Enter New Member Email: ")
                    members[member_id].update_information(name, email)
                    print("Member information updated successfully.")
                else:
                    print("Member not found.")
            except ValueError:
                print("Invalid input for Member ID. Please enter a number.")

        elif choice == "4":
            # Update Item Information
            try:
                item_id = int(input("Enter Item ID to update: "))
                if item_id in items:
                    price = float(input("Enter New Item Price: "))
                    in_stock = int(input("Enter New In-Stock Quantity: "))
                    items[item_id].update_stock_price(in_stock, price)
                    print("Item information updated successfully.")
                else:
                    print("Item not found.")
            except ValueError:
                print("Invalid input for Item ID, Price, or In-Stock. Please enter valid numbers.")

        elif choice == "5":
            # Add Item to Category
            item_id = int(input("Enter Item ID: "))
            category_name = input("Enter Category Name: ")
            if item_id in items and category_name in categories:
                categories[category_name].add_item(items[item_id])
                print("Item added to the category successfully.")
            else:
                print("Item or Category not found.")

        elif choice == "6":
            # Remove Item from Category
            item_id = int(input("Enter Item ID: "))
            category_name = input("Enter Category Name: ")
            if item_id in items and category_name in categories:
                items[item_id].categories.remove(categories[category_name])
                print("Item removed from the category successfully.")
            else:
                print("Item or Category not found.")

        elif choice == "7":
            # Process Transaction
            try:
                member_id = int(input("Enter Member ID: "))
                if member_id in members:
                    transaction_items = []
                    while True:
                        try:
                            item_id = int(input("Enter Item ID to add to the transaction (0 to finish): "))
                            if item_id == 0:
                                break
                            if item_id in items:
                                transaction_items.append(items[item_id])
                            else:
                                print("Item not found.")
                        except ValueError:
                            print("Invalid input for Item ID. Please enter a number.")
                    if transaction_items:
                        transaction = Transaction(members[member_id], transaction_items)
                        transactions.append(transaction)
                        total_spend = transaction.calculate_total()
                        print(f"Total spend in the transaction: ${total_spend}")
                    else:
                        print("No items in the transaction.")
                else:
                    print("Member not found.")
            except ValueError:
                print("Invalid input for Member ID. Please enter a number.")

        elif choice == "8":
            # List Items by Category
            category_name = input("Enter Category Name: ")
            if category_name in categories:
                items_in_category = inventory.list_items_by_category(category_name)
                print(f"Items in {category_name} category:")
                for item in items_in_category:
                    print(f"{item.name} - Price: ${item.price}, In-Stock: {item.in_stock}")
            else:
                print("Category not found.")

        elif choice == "9":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")
