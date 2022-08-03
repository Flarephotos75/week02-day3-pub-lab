from http import client
import unittest
from classes.customer import Customer
from classes.pub import Pub
from tests.customer_test import TestCustomer

class TestPub(unittest.TestCase):
    
    def setUp(self):
        self.pub = Pub("The Prancing Pony", 100.00, 15, 75, 15, 65)

    def test_pub_has_name(self):
        self.assertEqual("The Prancing Pony", self.pub.name)

    def test_till_amount(self):
        self.assertEqual(100, self.pub.till)

    def test_increase_till(self):
        self.pub.increase_till(2.5)
        expected = 102.50
        actual = self.pub.till
        self.assertEqual(expected, actual)

    def test_stock_level(self):
        self.assertEqual(15, self.pub.total_stock)

    def test_total_stock_value(self):
        self.assertEqual(75, self.pub.total_stock_value)

    def test_total_stock_food(self):
        self.assertEqual(15, self.pub.total_stock_food)

    def test_total_stock_value_food(self):
        self.assertEqual(65, self.pub.total_stock_value_food)

    def test_age_check(self):
        client = Customer(self)
        age_check = client.age_check(customer.john)
        self.assertEqual(True, age_check)