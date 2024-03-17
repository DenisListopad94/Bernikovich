class ProductManager:
    def __init__(self):
        self.products = {}

    def add_product(self, name, quantity):
        if name in self.products:
            self.products[name] += quantity
        else:
            self.products[name] = quantity

    def remove_product(self, name, quantity):
        if name in self.products:
            if self.products[name] >= quantity:
                self.products[name] -= quantity
                if self.products[name] == 0:
                    del self.products[name]
            else:
                print("Недостаточное количество товара для удаления")
        else:
            print("Товар не найден")

    def search_product(self, name):
        if name in self.products:
            return f"Товар '{name}' найден. Количество: {self.products[name]}"
        else:
            return "Товар не найден"