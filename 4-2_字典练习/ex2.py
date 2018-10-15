inventory = {
    '绳子':5,
    '火把':6,
    '金币':42,
    '匕首':1,
    '箭矢':12
}

def display_inventory(inventory):
    item_total = 0
    print("背包:")
    for name, number in inventory.items():
        print("{}x {}".format(number, name))
        item_total += number
    print("总道具数: {}".format(item_total))

display_inventory(inventory)
