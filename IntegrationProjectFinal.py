"""__author__ = Diego Grisales
# This program is designed to help retail cellphone stores control their daily
# cellphone inventory."""


def inventory():
    """This function calculates the total number of phones the user should
    have in their inventory"""
    total = 0
    print("Welcome to Inventory Control!  \nThis program is designed to help "
          "you control your cellphone inventory on a daily basis.")
    initialInventory = True
    while initialInventory:
        try:
            initialInventory = int(input("How many phones were in your "
                                         "inventory yesterday before opening "
                                         "the store? (Enter an integer): "))
        except ValueError:
            print("That is not an integer")
        else:
            break
    total += initialInventory
    sold = True
    while sold:
        try:
            sold = int(input("How many phones were sold yesterday? (Enter an "
                             "integer): "))
        except ValueError:
            print("That is not an integer")
        else:
            break
    total -= sold
    received = True
    while received:
        try:
            received = int(input("Did you receive any phones yesterday? if "
                                 "no phones received enter 0. (Enter an "
                                 "integer): "))
        except ValueError:
            print("That is not an integer")
        else:
            break
    total += received
    shipped = True
    while shipped:
        try:
            shipped = int(input("Were any phones shipped out to other stores "
                                "yesterday? if no phones shipped out enter 0. "
                                "(Enter an integer): "))
        except ValueError:
            print("That is not an integer")
        else:
            break
    total -= shipped
    print("You should have a total of", total, "phones in your inventory")
    return int(total)


def physical_inv():
    """This function compares the total of phones the user should have to
    the total of phones the user actually has. Then tells the user whether
    they are short, over or if they have a perfect inventory"""
    total = inventory()
    physicalInventory = True
    while physicalInventory:
        try:
            physicalInventory = int(input("How many phones were on your "
                                          "inventory before opening the store"
                                          " today? (Enter an integer): "))
        except ValueError:
            print("That is not an integer")
        else:
            break
    if physicalInventory != total:
        print("Verify that the information entered above is correct, "
              "and double check the total of phones in your inventory.")
    while total < physicalInventory:
        print("You are over", physicalInventory - total, "phones, enter the "
                                                         "correct amount of "
                                                         "phones in your "
                                                         "inventory.")
        physicalInventory = True
        while physicalInventory:
            try:
                physicalInventory = int(input("Re-enter the total amount of "
                                              "phones you counted physically "
                                              "before opening the store today:"
                                              " "))
            except ValueError:
                print("That is not an integer")
            else:
                break
        if total > physicalInventory:
            print("You are short", abs(physicalInventory - total), "phones, "
                                                                   "enter the "
                                                                   "correct "
                                                                   "amount of "
                                                                   "phones in "
                                                                   "your "
                                                                   "inventory")
            physicalInventory = True
            while physicalInventory:
                try:
                    physicalInventory = int(input("Re-enter the total amount "
                                                  "of phones you counted "
                                                  "physically before opening "
                                                  "the store today: "))
                except ValueError:
                    print("That is not an integer")
                else:
                    break
    while total > physicalInventory:
        print("You are short", abs(physicalInventory - total), "phones, enter "
                                                               "the correct "
                                                               "amount of "
                                                               "phones in your"
                                                               " inventory.")
        physicalInventory = True
        while physicalInventory:
            try:
                physicalInventory = int(input("Re-enter the total amount of "
                                              "phones you counted physically "
                                              "before opening the store "
                                              "today: "))
            except ValueError:
                print("That is not an integer")
            else:
                break
        if total < physicalInventory:
            print("You are over", physicalInventory - total, "phones, enter "
                                                             "the correct "
                                                             "amount of phones"
                                                             " in your "
                                                             "inventory.")
            physicalInventory = True
            while physicalInventory:
                try:
                    physicalInventory = int(input("Re-enter the total amount "
                                                  "of phones you counted "
                                                  "physically before opening "
                                                  "the store today: "))
                except ValueError:
                    print("That is not an integer")
                else:
                    break
    else:
        if total == physicalInventory:
            print("Perfect inventory!")


physical_inv()
