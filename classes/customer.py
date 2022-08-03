class Customer:
    def __init__(self, name, wallet, age, drunken_level):
        self.name = name
        self.wallet = wallet
        self.age = age
        self.drunken_level = drunken_level

    def age_check(self):
        return self.age >= 18

    # def buy_drink(self, drink):
    #     drink = 