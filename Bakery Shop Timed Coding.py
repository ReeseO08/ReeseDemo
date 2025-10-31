muffin_price = 5.95
kingcakeslice_price = 4.95
croissant_price = 3.95
scone_price = 3.75
sales_tax = 0.0945

print("Welcome to Boudreaux and Thibodeaux Bakery Shop")
print("--------------------------------------------------")
print("1. Muffin: $5.95")
print("2. King Cake Slices: $4.95")
print("3. Croissants: $3.95")
print("4. Scones: $3.75")
print ("-------------------------------------------------")

total = 0
order = input ("\nWhat would you like to order? Type the appropriate number of the menu item or DONE when order is complete:")

while order.upper() !="DONE":
    if order =="1":
        quantity = int(input("How many of that item would you like to order?:"))
        total += quantity * muffin_price
        print (f"You have ordered {quantity} muffin(s) for $5.95 each\n")
    elif order == "2":
        quantity = int(input("How many of that item would you like to order:"))
        total += quantity * kingcakeslice_price
        print(f"You have ordered {quantity} Kingcake(s) for $4.95 each\n")
    elif order == "3":
        quantity = int(input("How many of that item would you like to order:"))
        total += quantity *croissant_price
        print(f"You have ordered {quantity} Croissant(s) for $3.95 each\n")
    elif order == "4":
        quantity = int(input("How many of that item would you like to order:"))
        total += quantity * scone_price
        print(f"You have ordered {quantity} Scones(s) for $3.75 each\n")
    else:
        print("I'm sorry, that is not an appropriate response.")
    order = input("What would you like to order? Type the appropriate number of the menu item or DONE when order is complete:")

#Calulations 
total_with_tax = total + (total * sales_tax)
print ("-----------------------")
print (f"\nYour total is ${total_with_tax:.2f}")

