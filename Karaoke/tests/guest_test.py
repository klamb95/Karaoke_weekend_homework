import unittest
from src.guest import Guest


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Kieran", 10)


    def test_customer_has_name(self):
        self.assertEqual("Kieran", self.guest.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.guest.wallet)

    
        
