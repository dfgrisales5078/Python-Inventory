# Diego Grisales
# This program is designed to help retail cellphone stores control their daily cellphone inventory.

def inventory():
    total = 0
    print("Welcome to Inventory Control!  \nThis program is designed to help you control your cellphone inventory "
          "on a daily basis.")
    initialInventory = int(input("Enter the amount of cellphones you had in your inventory yesterday before you "
                                 "opened the store: "))

    total += initialInventory
    sold = int(input("How many phones were sold yesterday: "))
    total -= sold
    received = int(input("How many phones did you receive yesterday? if no phones received enter 0: "))
    total += received
    shipped = int(input("How many phones were shipped out to other stores yesterday, if no phones shipped out "
                        "enter 0: "))
    total -= shipped
    print("You should have a total of", total, "phones in your inventory")
    return int(total)


def physical_inv():
    total = inventory()
    physicalInventory = int(input("How many phones were on your inventory before opening the store today: "))
    if physicalInventory != total:
        print("Verify that the information entered above is correct, and double check the total of phones in your "
              "inventory.")
    while total < physicalInventory:
        print("You are over", physicalInventory - total, "phones, enter the correct amount of phones in your "
                                                         "inventory.")
        physicalInventory = int(input("Re-enter the total amount of phones you counted physically before opening the "
                                      "store today: "))
        if total > physicalInventory:
            print("You are short", abs(physicalInventory - total), "phones, enter the correct amount of phones in "
                                                                   "your inventory.")
            physicalInventory = int(input("Re-enter the total amount of phones you counted physically before opening "
                                          "the store today: "))
    while total > physicalInventory:
        print("You are short", abs(physicalInventory - total), "phones, enter the correct amount of phones in your "
                                                               "inventory.")
        physicalInventory = int(input("Re-enter the total amount of phones you counted physically before opening the "
                                      "store today: "))
        if total < physicalInventory:
            print("You are over", physicalInventory - total, "phones, enter the correct amount of phones in your "
                                                             "inventory.")
            physicalInventory = int(input("Re-enter the total amount of phones you counted physically before opening "
                                          "the store today: "))
    else:
        if total == physicalInventory:
            print("Perfect inventory!")


physical_inv()
