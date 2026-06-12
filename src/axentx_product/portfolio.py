from .product import Product

class Portfolio:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        if product not in self.products:
            self.products.append(product)

    def get_products(self):
        return self.products
