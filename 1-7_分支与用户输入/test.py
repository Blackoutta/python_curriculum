list = [1,2,3,4]

for i in list:
    if i == 1:
        print("   *")
    if i == 2:
        print("  ***")
    if i == 3:
        print(" *****")
    if i == 4:
        print("*******")

for i in list[::-1]:
    if i == 1:
        print("   *")
    if i == 2:
        print("  ***")
    if i == 3:
        print(" *****")
    if i == 4:
        print("*******")
