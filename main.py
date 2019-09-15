# Diego Grisales
# This program will be designed to help retail cellphone stores to control their daily cellphone inventory.
print("Welcome to Inventory Control!  \nThis program is designed to help you control your cellphone inventory daily.")
initialInventory = int(input("Enter the amount of cellphones you had in your inventory yesterday morning "
                             "before you opened the store: "))
sold = int(input("How many phones were sold yesterday: "))
received = int(input("Enter the amount of phones received yesterday, if no phones received enter 0: "))
shipped = int(input("Enter the amount of phones shipped out to another store yesterday :"))
print("You should have", initialInventory - sold + received - shipped, "phones today before opening the store.")
