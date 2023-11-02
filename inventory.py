import random
import random
def possible_items():
    items = {
        "swords": ["sword1", "sword2", "sword3"],
        "potions": ["healing", "speed", "strength", "luck"],
        "keys": ["chest key", "heart key"],
    }
    return items

def random_item(item_type):
    items = possible_items()
    if item_type in items and items[item_type]:
        return random.choice(items[item_type])
    else:
        print(f"No items of type '{item_type}' available.")
        return None

def create_inventory():
    inventory = {
        "swords": [],
        "shields": [],
        "potions": [],
        "gold": 0
    }
    return inventory

def display_inv(inventory_data):
    print("INVENTORY:")
    for item, name in inventory_data.items():
        print(f"{item}: {name}")

def check_empty_inventory(inventory_data):
    for category, items in inventory_data.items():
        if category != "gold" and items:  
            return False  
    return True  

def add_gold(inventory_data, amount):
    inventory_data["gold"] += amount