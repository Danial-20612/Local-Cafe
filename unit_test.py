import pytest 
from local_cafe import End_Users
import unittest

class TestMenuItems(unittest.TestCase):
    def setUp(self):
        class Menu_Food:
            def __init__(self, name, price):
                self.name = name
                self.price = price

        class Menu_Items:
            def __init__(self):
                self.items = [
                    Menu_Food("Pizza", 22),
                    Menu_Food("Burger", 4.50),
                    Menu_Food("Pasta", 5.10),
                ]

        self.Menu_Food = Menu_Food
        self.Menu_Items = Menu_Items
        self.menu = Menu_Items()

    # 
    def test_first_item_name_pass(self):
        self.assertEqual(self.menu.items[0].name, "Pizza")  # True

    #
    def test_first_item_name_fail(self):
        self.assertEqual(self.menu.items[0].name, "Burger")  # False

if __name__ == "__main__":
    unittest.main()


