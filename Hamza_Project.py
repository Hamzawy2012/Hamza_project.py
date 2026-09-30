menu={"Meat":100,"Chicken":80,"Rice":40,"Fish":60}
def get_valid_price(prompt):
    while True:
        try:
            price = int(input(prompt))
            if price < 0:
                print("price cannot be either negative or zero")
            else:
                return price
        except ValueError:
            print("invalid input")
def add_item():
    name = input("Enter a food name :".capitalize())
    price = get_valid_price("Enter a price :")
    if name in menu:
        print("item is already in menu")
    else:
        menu[name] = price
        print("item added to menu")
def remove_item():
    item=input('Enter an item to remove :').capitalize()
    if item in menu:
        menu.pop(item)
        print(f"{item} removed from menu")
    elif item not in menu:
        print(f"{item} is not in menu")
def change_price():
    changed = input("Enter a food name to change its price :").capitalize()
    changed_price=0
    if  changed in menu:
        changed_price = input("Enter a new price :")
        while not changed_price.isdigit() or int(changed_price) <= 0:
            print("invalid input")
            changed_price = (input("Enter a new price :"))
        if int(changed_price) == menu[changed]:
            print("price is already in menu")
        if int(changed_price) != menu[changed]:
            print("added price to menu")
    else:
        print(f"{changed} is not in menu")
def show_menu():
    input_organized = input("Do you want to organize the menu by name or price (n/p): ").strip().lower()
    if input_organized == "p":    
        organized_menu = sorted(menu.items(), key=lambda x: x[1])
    if input_organized == "n":
        organized_menu = sorted(menu.items())
    print(organized_menu)
def find_item():
    item = input("Enter a food name to to search for :").capitalize()
    if item in menu:
        print("item found in menu")
        print(f"{item} : {menu[item]}")
    else:
        print("item not found in menu")
def summary():
    length = len(menu)
    print(f"Total number of items in menu {length}")
    menu_values = menu.values()
    total_price = sum(menu_values)
    print(f"Total price of all items in menu {total_price}")
def clear_menu():
    menu.clear()
    print("menu cleared")
def main():
    while True:
        print("\nMenu Management System")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Change Price")
        print("4. Show Menu")
        print("5. Find Item")
        print("6. Summary")
        print("7. Clear Menu")
        print("8. Exit")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_item()
        elif choice == "2":
            remove_item()
        elif choice == "3":
            change_price()
        elif choice == "4":
            show_menu()
        elif choice == "5":
            find_item()
        elif choice == "6":
            summary()
        elif choice == "7":
            clear_menu()
        elif choice == "8":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")
main()

