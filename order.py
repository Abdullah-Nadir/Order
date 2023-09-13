# Importing exit function from system library
from sys import exit

# Storing the menu in a dictionary
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Creating an empty list for storing items
items = []

# Creating an infinite loop
while True:
    try:
        # Taking input from the user
        item = input("Item: ").title()
    except EOFError: # Handling the ctrl-d case
        print()
        exit()
    else:
        bill = 0
        if item in menu:
            items.append(item)
            for item in items:
                bill += menu[item]
            print(f"Total: ${bill:.2f}")


