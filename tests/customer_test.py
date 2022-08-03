import unittest
from classes.customer import Customer

class TestCustomer(unittest.TestCase):
    
    def setUp(self):
        self.stephen = Customer("Stephen", 20, 30, 0)
        self.john = Customer("John", 40, 25, 0)
        self.adam = Customer("Adam", 10, 17, 0)

    def test_get_customer_name(self):
        self.assertEqual("Stephen", self.stephen.name)

    def test_get_customer_wallet(self):
        self.assertEqual(40, self.john.wallet)

    def test_get_customer_age(self):
        self.assertEqual(17, self.adam.age)

    def test_get_drunken_level(self): 
        self.assertEqual(0, self.stephen.drunken_level)

    # def test_age_check(self):
    #     age_check = self.john.age_check()
    #     self.assertEqual(True, age_check)