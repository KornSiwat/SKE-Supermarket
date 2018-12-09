class Item():
    ID = 0
    def __init__(self,name,price):
        self.id = self.ID + 1
        self.name = name
        self.price = price
        Item.ID += 1

    def __str__(self):
        return f"{self.name} price {self.price}"

class Customer():
    ID = 0
    def __init__(self):
        self.id = self.ID + 1
        self.cart = []
        Customer.ID += 1

    def add_item(self, item):
        self.cart.append(item)

    def total(self):
        total = 0
        for item in self.cart:
            total += int(item.price)
        return total

    def print_total_details(self):
        for number,item in enumerate(self.cart):
            print(f"\n\t{number+1}).{item.name} Price: {item.price} Baht")
        print(f"\n\tTotal: {self.total()}")

    def __str__(self):
        return f'{self.cart}'

class Cashier():
    ID = 0
    def __init__(self):
        self.id = self.ID + 1
        self.customer = None
        self.history_path = f'cashier_{self.ID}.txt'
        path = open( f'./cashier/{self.history_path}', 'w')
        path.write(f"Transaction History of Cashier {self.ID}\n")
        path.close()
        Cashier.ID += 1
        self.status = 'available'

    def add_customer(self, customer):
        if self.customer == 'unavailable':
            raise ValueError('cashier is not available')
        self.customer = customer
        self.status = 'unavailable'

    def paid(self):
        path = open( f'./cashier/{self.history_path}', 'a')
        path.write(f"\nCustomer: {self.customer.id}\n")
        for number,item in enumerate(self.customer.cart):
            path.write(f"\n\t{number+1}).{item.name} Price: {item.price} Baht")
        path.write(f"\n\n\tTotal: {self.customer.total()}")
        path.close
        self.customer = None
        self.status = 'available'

    def receipt(self):
        self.customer.print_total_details()
        

if __name__ == "__main__":
    C1 = Cashier()
    lay = Item('lay',20)
    Korn = Customer()
    Korn.add_item(lay)
    C1.add_customer(Korn)
    C1.paid()
    