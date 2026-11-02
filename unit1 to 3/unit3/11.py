# 3.11 Inventory System
inventory = {}

def add_item(name, qty):
    inventory[name] = inventory.get(name, 0) + qty

def remove_item(name):
    if name in inventory:
        del inventory[name]
    else:
        print(f"Item '{name}' not found.")

def update_qty(name, qty):
    if name in inventory:
        inventory[name] = qty
    else:
        print(f"Item '{name}' does not exist.")

def display_inventory():
    print(f"\n{'Item':<15} | {'Quantity':<10}")
    print("-" * 28)
    for name, qty in inventory.items():
        print(f"{name:<15} | {qty:<10}")

def low_stock():
    low = {name: qty for name, qty in inventory.items() if qty < 5}
    print(f"\nLow Stock Items (<5): {low if low else 'None'}")


# Simulation
add_item("Notebooks", 15)
add_item("Pens", 3)
add_item("Erasers", 2)
add_item("Markers", 10)

display_inventory()
low_stock()

update_qty("Pens", 12)
remove_item("Erasers")

print("\n--- After Modifications ---")
display_inventory()