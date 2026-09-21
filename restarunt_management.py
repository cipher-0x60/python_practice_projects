menu = {
    'Pizza':40,
    'Pasta':30,
    'Burger':60,
    'Salad':70,
    'Coffee':80,
}

print("Welcome to the PYTHON Restaurant")
print(f"Menu: {menu}")


order_total = 0
items_added = []

while True:
    item = input("\nEnter the name of item you want to order = ")
    
    if item in menu:
        order_total += menu[item] 
        items_added.append(item)
        print(f"Your Item {item} Has Been Added to you order. ₹")
    else:
        print(f"Order item {item} is not available yet!")

    
    another_order = input("Do you want to add another item? (Yes/No) ")
    
    if another_order != "Yes":
        break

print(f"\nYour Total Amount of Orders for ({', '.join(items_added)}) is RS.{order_total}")