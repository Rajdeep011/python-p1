#Define the menu of the restaurant
menu = {
    'Pizza': 40,
    'Pasta': 50,
    'Burger': 50,
    'Coldcoffe': 80,
    'Fries': 60,
    'Salad': 80,
}

#Greet
print("Welcome to PYTHON Restaurant")
print(" Pizza: Rs40\n Pasta: Rs50\n Burger: Rs50\n Coldcoffe: Rs80\n Fries: Rs60\n Salad: Rs80")

order_total = 0
#80 + 80 = 160

item_1 = input("Enter the name of item you wanna order = ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your item {item_1} has been added to your order")

else: 
    print(f"Ordered item {item_1} is not available yet")  


another_order = input("Do you wanna add another item? (Yes/No) ") 

if another_order == "Yes":

    item_2 = input("Enter the name of your second item = ")

    if item_2 in menu:
        order_total += menu[item_2]
        print(f"your item {item_2} has been added to your list")

    else:
     print(f"Ordered item {item_2} is not available!")  


print(f"The total amount of items to pay {order_total}")           

