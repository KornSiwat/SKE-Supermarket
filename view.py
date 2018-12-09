from model import Item,Customer,Cashier
import os

item_list = {}
path = open( './item/item.txt', 'r')
data = path.read().splitlines()
path.close()
data = data[1::]
data = [x.split(',') for x in data if x != '']
for element in data:
    item_list[element[0]] = Item(element[0],int(element[1]))
print('Item List: ')
item_keys = []
for index,key in enumerate(item_list):
    item_keys.append(key)
    print(f'\t{index+1}){item_list[key].name} {item_list[key].price}')
cashier_list = {}
raw = open('./cashier/cashier_no.txt' , 'r')
total_cashier = int(raw.read())
raw.close()
while Cashier.ID < total_cashier:
    cashier_list[Cashier.ID] = Cashier()

def clear_screen():
    try:
        os.system('clear')
    except Exception:
        pass

def router(route):
    if route == 'main_menu':
        clear_screen()
        menu_choice = main_menu()
        return menu_choice
    elif route == 'manager_menu':
        clear_screen()
        menu_choice = manager_menu()
        return menu_choice
    elif route == 'customer_menu':
        clear_screen()
        menu_choice = customer_menu()
        return menu_choice
    elif route == 'manage_item':
        clear_screen()
        menu_choice = manage_item()
        return menu_choice
    elif route == 'manage_cashier':
        clear_screen()
        menu_choice = manage_cashier()
        return menu_choice
    elif route == 'add_cashier':
        clear_screen()
        menu_choice = add_cashier()
        return menu_choice
    elif route == 'remove_cashier':
        clear_screen()
        menu_choice = remove_cashier()
        return menu_choice
    elif route == 'add_item':
        clear_screen()
        menu_choice = add_item()
        return menu_choice
    elif route == 'view_item':
        clear_screen()
        menu_choice = view_item()
        return menu_choice
    elif route == 'add_to_cart':
        menu_choice = add_to_cart()
        return menu_choice
    elif route == 'cart':
        clear_screen()
        menu_choice = cart()
        return menu_choice
    elif route == 'checkout':
        clear_screen()
        menu_choice = checkout()
        return menu_choice
    elif route == 'choose_cashier':
        clear_screen()
        menu_choice = choose_cashier()
        return menu_choice
    elif route == 'customer_menu':
        clear_screen()
        menu_choice = customer_menu()
        return menu_choice
    
def main_menu():
    print("Welcome To SKE Supermarket")
    print("Choose Your Duty")
    print("\t 1) Manager")
    print("\t 2) Customer")
    menu_choice = {
        1: 'manager_menu',
        2: 'customer_menu'
    }
    return menu_choice

def manager_menu():
    print("Manager Site")
    print("Choose Your Action")
    print("\t 1) Manage Item")
    print("\t 2) Manage Cashier")
    print("\t 0) Main Menu")
    menu_choice = {
        1: 'manage_item',
        2: 'manage_cashier',
        0: 'main_menu'
    }
    return menu_choice

def manage_item():
    print("Item Management")
    raw = open('./item/item.txt' , 'r')
    item = raw.read().splitlines()
    print('')
    for line in item:
        print(line)
    print('')
    print("Choose Your Action")
    print("\t 1) Add")
    print("\t 2) Remove")
    print("\t 9) Manager Menu")
    print("\t 0) Main Menu")
    raw.close()
    menu_choice = {
        1: 'add_item',
        2: 'manage_cashier',
        9: 'manager_menu',
        0: 'main_menu'
    }
    return menu_choice

def manage_cashier():
    Cashier.ID = len(cashier_list)
    print("Cashier Management")
    try:
        raw = open('./cashier/cashier_no.txt' , 'r')
        total_cashier = int(raw.read())
        raw.close()
    except Exception as exp:
        print(exp)
        raw = open('./cashier/cashier_no.txt' , 'w')
        raw.write("0")
        raw.close()
        total_cashier = 0
    print(f'Total Cashier: {total_cashier}')
    print("Choose Your Action")
    print("\t 1) Add")
    print("\t 2) Remove")
    print("\t 9) Manager Menu")
    print("\t 0) Main Menu")
    raw.close()
    menu_choice = {
        1: 'add_cashier',
        2: 'remove_cashier',
        9: 'manager_menu',
        0: 'main_menu'
    }
    return menu_choice

def add_cashier():
    Cashier.ID = len(cashier_list)
    cashier_list[Cashier.ID] = Cashier()
    raw = open('./cashier/cashier_no.txt' , 'r')
    raw.close()
    raw = open('./cashier/cashier_no.txt' , 'w')
    raw.write(str(Cashier.ID))
    raw.close()
    menu_choice = manage_cashier()
    return menu_choice

def remove_cashier():
    Cashier.ID = len(cashier_list)
    del cashier_list[Cashier.ID]
    Cashier.ID -= 1
    raw = open('./cashier/cashier_no.txt' , 'r')
    total_cashier = int(raw.read())
    raw.close()
    raw = open('./cashier/cashier_no.txt' , 'w')
    raw.write(str(total_cashier-1))
    raw.close()
    menu_choice = manage_cashier()
    return menu_choice
    

def add_item():
    name = input('name: ')
    price = input('price: ')
    path = open( './item/item.txt', 'a')
    path.write(f'\n{name},{price}')
    path.close()
    menu_choice = manage_item()
    return menu_choice

def customer_menu():
    path = open('customer_no.txt', 'r')
    customer_no = int(path.read())
    path.close()
    Customer.ID = customer_no + 1
    global customer
    customer = Customer()
    path = open('customer_no.txt', 'w')
    path.write(f'{customer.ID}')
    path.close()
    print(f"Customer Site No.{customer.ID}")
    print("Choose Your Action")
    print("\t 1) View Item")
    print("\t 2) Your Cart")
    print("\t 3) Check out")
    print("\t 0) Main Menu")
    menu_choice = {
        1: 'view_item',
        2: 'cart',
        3: 'checkout',
        0: 'main_menu'
    }
    return menu_choice

def view_item():
    path = open( './item/item.txt', 'r')
    data = path.read().splitlines()
    path.close()
    data = data[1::]
    data = [x.split(',') for x in data if x != '']
    global item
    item = {}
    for element in data:
        item[element[0]] = Item(element[0],element[1])
    print('Item List: ')
    global keys
    keys = []
    for index,key in enumerate(item):
        keys.append(key)
        print(f'\t{index+1}){item[key].name} {item[key].price}')
    print("Choose Your Action")
    print("\t 1) Add Item To Cart")
    print("\t 2) Your Cart")
    print("\t 3) Check out")
    print("\t 0) Main Menu")
    menu_choice = {
        1: 'add_to_cart',
        2: 'cart',
        3: 'checkout',
        0: 'main_menu'
    }
    return menu_choice

def add_to_cart():
    product_id = int(input('Product No: '))
    customer.add_item(item[keys[product_id-1]])
    menu_choice = view_item()
    return menu_choice

def cart():
    print("Cart")
    print("Item List:")
    for index,elem in enumerate(customer.cart):
        print(f'\t{index+1}){elem}')
    print("Choose Your Action")
    print("\t 1) Check out")
    print("\t 9) Customer Menu")
    print("\t 0) Main Menu")
    menu_choice = {
        1: 'checkout',
        9: 'customer_menu',
        0: 'main_menu'
    }
    return menu_choice

def checkout():
    print("Cashier Available")
    print("List:")
    for index,key in enumerate(cashier_list):
        print(f'\tCashier No.{index+1} Status: {cashier_list[key].status}')
    print("Choose Your Action")
    print("\t 1) Choose Cashier")
    print("\t 9) Customer Menu")
    print("\t 0) Main Menu")
    menu_choice = {
        1: 'choose_cashier',
        9: 'customer_menu',
        0: 'main_menu'
    }
    return menu_choice

def choose_cashier():
    cashier_no = int(input("Cashier No.: "))
    cashier_list[cashier_no].add_customer(customer)
    cashier_list[cashier_no].receipt()
    cashier_list[cashier_no].paid()
    print("Thank You")
    print("Choose Your Action")
    print("\t 0) Main Menu")
    menu_choice = {
        0: 'main_menu'
    }
    return menu_choice

        


if __name__ == "__main__":
    path = open( 'item.txt', 'r')
    data = path.read().splitlines()
    path.close()
    data = data[1::]
    data = [x.split(',') for x in data if x != '']
    item = {}
    for element in data:
        item[element[0]] = Item(element[0],element[1])
    print(item)