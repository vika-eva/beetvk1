
class Product:

    def __init__(self, type_: str, name: str, price: float):
        assert price >= 0
        self.product_id = id(self)
        self.type_ = type_
        self.name = name
        self.price = price
        self.amount = 0

    def __repr__(self):
        return f"{self.type_}: {self.name} {self.price}"


class ProductStore:

    def __init__(self):
        self.products = []
        self.amount = 0
        self.price = 0

    def __str__(self):
        return f"кол-во {self.amount},продук {self.products},цена {self.price}"

    def add(self, product, amount):
        self.product = Product(product.type_, product.name, product.price)
        # self.product = Product(product.type_, product.name, product.price)
        # self.products.append(product.name)
        self.amount += amount
        self.price += 30
        self.products.append({"product": product, "amount": amount})
        return self

    def set_discount(self, identifier, percent, identifier_type="name"):
        for identifier in self.products:
            if identifier == identifier:
                self.price -= percent
                return self
            else:
                raise ValueError

    def sell_product(self, product_name, amount):
        for product_name in self.products:
            if product_name == product_name:
                self.amount -= amount
        if product_name not in self.products:
            raise ValueError("error")

    def get_income(self):
        total = sum(item["product"].price * item["amount"] for item in self.products)
        return total


    def get_all_products(self):
        return self.products


    def get_product_info(self, product_name):
        for product_name in self.products:
            if product_name == product_name:
                return self
            else:
                raise ValueError("error")


# p = Product("sport", "cross", 5)
# s = ProductStore()
# s.add(p, 58)
# s.add(p, 90)
# print(s.add(p, 10))
# s.set_discount(p, 6)
# g = Product("eat", "reeee", 67.5)
# prod1 = ProductStore()
# prod1.add(g, 100)
# print(prod1.amount)
# prod1.sell_product(g, 5)
# print(prod1.amount)
# print(prod1.price)
# prod1.set_discount(g, 5)
# print(prod1.price)
# prod1.get_income()
# print(prod1.get_all_products())
# print(s.get_all_products())
# prod1.get_product_info("reeee")
# print(prod1.get_all_products())
# prod1.get_income()
# print(prod1.get_income())