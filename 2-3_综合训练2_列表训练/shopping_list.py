import os
# infinite loop and how to break it or continue it
# Create a new empty list named shopping_list
shopping_list = []

#Create a function named add_to_list that declares a parameter named item
    #Add the item to the list

def clear_screen():
    os.system('cls')

def add_to_list(item):
    shopping_list.append(item)
    # notify user that the item was add and state the number of items in the list currently
    input("添加成功, 您目前的清单中有 {} 件物品!".format(len(shopping_list)))

# Define a function named show_list that prints all the items in the list
def show_list():
    for item in shopping_list:
        print("* " + item)

def show_help():
    print("今天要买点什么呢")
    print("""
输入 "DONE" 来完成清单
输入 'HELP' 来查看该帮助
输入 'LIST' 来查看当前购物清单
""")


while True:
    clear_screen()
    show_help()
    new_item = input("> ")
    if new_item == '':
        input("输入不能为空！")
        continue
    elif new_item.upper() == 'DONE':
        break
    elif new_item.upper() == 'HELP':
        show_help()
        continue
    elif new_item.upper() == 'LIST':
        print("===> 您现在的购物清单中有以下物品: <===")
        show_list()
        input()
        continue
    else:
        add_to_list(new_item)

show_list() # when uswer is done
    # Call add_to_list with new_item
