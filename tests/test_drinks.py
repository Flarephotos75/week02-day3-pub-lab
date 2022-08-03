import unittest
from classes.drink import Drink

class TestDrinks(unittest.TestCase):
    
    def setUp(self):
        self.beer = Drink("Stella", 4, 5, 2)
        self.wine = Drink("Pinot Grigio", 5, 5, 4)
        self.gin = Drink("Gordon's", 6, 5, 5)

    def test_get_drink_name(self):
        self.assertEqual("Stella", self.beer.name)

    def test_get_drink_price(self):
        self.assertEqual(5, self.wine.price)

    def test_get_drink_stock(self):
        self.assertEqual(5, self.gin.stock)

    def test_get_drink_units(self): 
        self.assertEqual(4, self.wine.units)