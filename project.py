import sys
import csv
from customer import Customer, Order
from setup_db import initalize_db

from tabulate import tabulate

# Orderly: restaurant menu ordering system
def main():
    initalize_db()
    while True:
        print(main_menu())
        try:
            inp = int(input("Enter your choice: "))
            if inp == 1:
                handle_returning_customer()
            elif inp == 2:
                handle_new_customer()
            elif inp == 3:
                sys.exit("Thank you for visiting!")
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Input is not a number. Try again.")


# Main menu display
def main_menu():
    return "Welcome to Orderly!\n1. Returning Customer\n2. New Customer\n3. Exit"


# Handle returning customer
def handle_returning_customer():
    phone = input("Enter your phone number: ")
    customer_id = Customer.get_customer_id(phone)
    if customer_id is None:
        print("Customer not found. Please register as a new customer.")
    else:
        order_items, total_price = get_order()
        order = Order(customer_id, ', '.join(order_items), total_price)
        order.save_to_db()
        print(f"Order placed successfully! Total: ${total_price}")


#Handle new customer
def handle_new_customer():
    name = input("Name: ")
    phone = input("Phone number: ")
    customer = Customer(name, phone)
    customer.save_to_db()
    customer_id = Customer.get_customer_id(phone)
    order_items, total_price = get_order()
    order = Order(customer_id, ', '.join(order_items), total_price)
    order.save_to_db()
    print(f"Order placed successfully! Total: ${total_price}")


# Displays menu by reading and showing menu.csv
def display_menu():
    try:
        with open("menu.csv") as file:
            reader = csv.reader(file)
            print()
            menu = tabulate(reader, headers="firstrow", tablefmt="grid")
            return menu

    except FileNotFoundError:
        sys.exit("File does not exist")


# Reads csv and adds items in menu to a dictionary
def get_menu_from_csv():
    menu = {}
    try:
        with open("menu.csv") as file:
            reader = csv.DictReader(file)
            for row in reader:
                item = row["Item"]
                price = row["Price"]
                menu[item] = float(price.replace('$', ''))
        return menu
    except FileNotFoundError:
        sys.exit("File does not exist")



# Get order from the customer
def get_order():
    order_items = []
    total_price = 0
    menu = get_menu_from_csv()
    menu_list = list(menu.items())

    print(display_menu())

    while True:
        try:
            choice = int(input("Enter the menu item number to add to order (0 to finish): "))
            if choice == 0:
                break
            if 1 <= choice <= len(menu_list):
                item, price = menu_list[choice - 1]
                order_items.append(item)
                total_price += price
                print(f"Added {item} - ${price}")
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Enter a number. Try again.")
    
    return order_items, total_price


if __name__ == "__main__":
    main()

