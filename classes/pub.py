class Pub:
    def __init__(self, name, till, total_stock, total_stock_value, total_stock_food, total_stock_value_food):
        self.name = name
        self.till = till
        self.total_stock = total_stock
        self.total_stock_value = total_stock_value
        self.total_stock_food = total_stock_food
        self.total_stock_value_food = total_stock_value_food

    def increase_till(self, amount):
        self.till += amount