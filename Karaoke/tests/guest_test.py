import unittest
from src.guest import Guest
from src.rooms import Rooms


class TestGuest(unittest.TestCase):

    def setUp(self):
        self.guest = Guest("Kieran", 10)
        self.rooms_1 = Rooms("Blue Room", 4, 20.00)

    def test_customer_has_name(self):
        self.assertEqual("Kieran", self.guest.name)

    def test_customer_has_wallet(self):
        self.assertEqual(10, self.guest.wallet)

    def test_customer_can_afford(self):
        self.assertEqual(True, self.guest.customer_can_afford(self.rooms_1))

    def test_customer_cant_afford(self):
        self.poor_guest = Guest("Adam", 0)
        self.assertEqual(False, self.poor_guest.customer_can_afford(self.rooms_1))

    def test_customer_can_pay_entry(self):
        rooms_1 = Rooms("Blue Room", 4, 20.00)
        self.guest.pay_entry_fee(rooms_1)
        self.assertEqual(9, self.guest.wallet)
 

    
        
