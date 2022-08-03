import unittest
from classes.food import Food

class TestFood(unittest.TestCase):
    
    def setUp(self):
        self.chicken = Food("chicken", 5, 5, 2)
        self.burger = Food("burger", 6, 5, 4)
        self.chips = Food("chips", 2, 5, 1)

    def test_get_food_name(self):
        self.assertEqual("chicken", self.chicken.name)

    def test_get_food_price(self):
        self.assertEqual(6, self.burger.price)

    def test_get_food_stock_level(self):
        self.assertEqual(5, self.chips.stock_level)

    def test_get_rejuvenation_level(self): 
        self.assertEqual(4, self.burger.rejuvenation)