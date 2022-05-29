import unittest

from src.guests import Guest
from src.rooms import Room


class TestGuest(unittest.TestCase):
    def setUp(self):
        self.guest = Guest("Steven Seagal", 10.00)
        self.guest_2 = Guest("Jeremey Clarkson", 10.00)

    def test_has_guest(self):
        self.assertEqual("Steven Seagal", self.guest.name)

    def test_has_wallet(self):
        self.assertEqual(10.00, self.guest.wallet)

    def test_can_guest_pay_for_room(self):
        room = Room("1", 5.00, 10, 100)
        self.guest.buy_room(room)
        self.assertEqual(5.00, self.guest.wallet)
