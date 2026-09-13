class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def get_total(self):
        return self.price * self.quantity

class Bill:
    def __init__(self):
        self.products = []
    
    def add_product(self, product):
        self.products.append(product)

    def calculate_total(self):
        total = sum(p.get_total() for p in self.products)
        tax = total * 0.05  # 5% tax
        return total, tax, total + tax

    def display_bill(self):
        print("\n--- FINAL BILL ---")
        print(f"{'Name':<10} {'Price':<10} {'Qty':<10} {'Total'}")
        print("-"*40)
        for p in self.products:
            print(f"{p.name:<10} {p.price:<10} {p.quantity:<10} {p.get_total()}")
        print("-"*40)
        total, tax, grand = self.calculate_total()
        print(f"Total: {total}")
        print(f"Tax (5%): {tax}")
        print(f"Grand Total: {grand}")

# Example
bill = Bill()
bill.add_product(Product("Pen", 10, 5))
bill.add_product(Product("Book", 50, 2))
bill.display_bill()