import unittest
from src.rooms import Rooms
from src.guest import Guest
from src.songs import Songs

class TestRooms(unittest.TestCase):

 
    def setUp(self):
        self.rooms = Rooms("Blue Room")
        self.guest_1 = Guest("Kieran", 10)

    def test_rooms_has_name(self):
        self.assertEqual("Blue Room", self.rooms.room_name)


    def test_rooms_number_starts_at_0(self):
        self.assertEqual(0, self.rooms.number_in_room())

    #PDA example
    def test_add_person_to_room(self):
        self.rooms.add_person_to_room(self.guest_1)
        self.assertEqual(1, self.rooms.number_in_room())

    def test_remove_person_from_room(self):
        self.rooms.add_person_to_room(self.guest_1)
        self.rooms.remove_person(self.guest_1)
        self.assertEqual(0, self.rooms.number_in_room())

  


