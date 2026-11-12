"""HW0: a game inventory. Practises Session 1: names and objects, defaults, *args, comprehensions."""


def add_item(inventory, item, count=1):
    new_inventory = inventory.copy()
    new_inventory[item] = new_inventory.get(item, 0) + count
    return new_inventory


def total_items(*inventories):
    return sum(sum(inventory.values()) for inventory in inventories)


def running_low(inventory, limit=2):
    return sorted([item for item, count in inventory.items() if count < limit])
