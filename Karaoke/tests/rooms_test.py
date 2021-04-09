import unittest
from src.rooms import Rooms
from src.guest import Guest
from src.songs import Songs

class TestRooms(unittest.TestCase):

    def setUp(self):
        self.rooms = Rooms("Blue Room")

    def test_rooms_has_name(self):
        self.assertEqual("Blue Room", self.rooms.room_name)


