# Diego Grisales
# This program will be designed to help retail cellphone stores to control their daily cellphone inventory.


print("Welcome to Inventory Control!  \nThis program is designed to help you control your cellphone inventory daily.")
initialInventory = int(input("Enter the amount of cellphones you had in your inventory yesterday morning "
                             "before you opened the store: "))
sold = int(input("How many phones were sold yesterday: "))
received = int(input("Enter the amount of phones received yesterday, if no phones received enter 0: "))
shipped = int(input("Enter the amount of phones shipped out to another store yesterday, if no phones shipped out "
                    "enter 0: "))
finalInventory = initialInventory - sold + received - shipped
print("You should have", finalInventory, "phones today before opening the store.")

physicalInventory = int(input("Enter the total amount of phones you counted physically before opening the store today: "))
if finalInventory == physicalInventory:
    print("Perfect inventory!")
elif physicalInventory > finalInventory:
    print("You are over", physicalInventory - finalInventory, "phones, make sure you counted properly and entered the "
                                                              "correct amounts above.")
else:
    if physicalInventory < finalInventory:
        print("You are short", physicalInventory - finalInventory, "phones, make sure you counted properly and "
                                                                   "entered the correct amounts above.")
