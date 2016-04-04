"""CP1804 Assignment 1 - 2016
   Items for Hire - Solution
   Michael Gonzalez
   7/4/2016

Pseudocode:

# function_main()
# Load CSV
# Display welcome message
# Display menu
# Get choice
# While choice is not “q”
# 	If choice is ‘l’
# 		Display  list(items.csv)
# 	Else if choice is ‘h’
# 		Call hireitem()
# 	Else if choice is ‘r’
# 		Call returnitem()
# 	Else if choice is ‘a’
# 		Call additem()
# 	Else
# 	Display(“Invalid selection,  please choose a valid letter from the menu”)
# print goodbye message"""

MENU = "\nMenu:\n(L)sit an item\n(H)ire an item\n(R)eturn an item\n(A)dd an item\n(Q)uit"
def main():
    print("Welcome to items for hire rental system")
    print("Written by Michael Gonzalez 2016")
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q" or "q":
        if choice == "L" or "l":
            print('items.csv')
        elif choice == "H" or "h":
            hireitem()
        elif choice == "R" or "r":
            returnitem()
        elif choice == "A" or "a":
            additem()