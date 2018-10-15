inventory = {
    '金币': 42,
    '绳子': 1
}

dragon_loot = ['金币', '匕首', '金币', '金币', '红宝石']

def display_inventory(inventory):
    item_total = 0
    print("背包:")
    for name, number in inventory.items():
        print("{}x {}".format(number, name))
        item_total += number
    print("总道具数: {}".format(item_total))

def add_to_inventory(inventory, loot):
    for item in loot:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory

inventory = add_to_inventory(inventory, dragon_loot)
display_inventory(inventory)
