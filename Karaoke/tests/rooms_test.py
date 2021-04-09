import unittest
from src.rooms import Rooms
from src.guest import Guest
from src.songs import Songs

class TestRooms(unittest.TestCase):

 
    def setUp(self):
        self.rooms_1 = Rooms("Blue Room", 10)
        self.rooms_2 = Rooms("Green Room", 8)

        self.guest_1 = Guest("Kieran", 10)
        self.guest_2 = Guest("Aidan", 8)

        self.songs_1 = Songs("Dive", "Ed Sheeran")
        self.songs_2 = Songs("fix You", "Coldplay")


        

    def test_rooms_has_name(self):
        self.assertEqual("Blue Room", self.rooms_1.room_name)


    def test_rooms_number_starts_at_0(self):
        self.assertEqual(0, self.rooms_1.number_in_room())

    #PDA example
    def test_add_person_to_room(self):
        self.rooms_1.add_person_to_room(self.guest_1)
        self.assertEqual(1, self.rooms_1.number_in_room())

    def test_add_2_people_to_room(self):
        self.rooms_1.add_person_to_room(self.guest_1)
        self.rooms_1.add_person_to_room(self.guest_2)
        self.assertEqual(2, self.rooms_1.number_in_room())

    def test_remove_person_from_room(self):
        self.rooms_1.add_person_to_room(self.guest_1)
        self.rooms_1.remove_person(self.guest_1)
        self.assertEqual(0, self.rooms_1.number_in_room())

    def test_songs_starts_at_0(self):
        self.assertEqual(0, self.rooms_1.songs_in_queue())

    def tests_add_song_to_queue(self):
         self.rooms_1.add_song_to_queue(self.songs_1)
         self.assertEqual(1, self.rooms_1.songs_in_queue())

    def tests_add_songs_to_queue(self):
        self.rooms_1.add_song_to_queue(self.songs_1)
        self.rooms_1.add_song_to_queue(self.songs_2)
        self.assertEqual(2, self.rooms_1.songs_in_queue())

    def tests_remove_songs_from_queue(self):
        self.rooms_1.add_song_to_queue(self.songs_1)
        self.rooms_1.remove_songs_from_queue(self.songs_1)
        self.assertEqual(0, self.rooms_1.songs_in_queue())

    def tests_room_has_capacity(self):
        self.assertEqual(10, self.rooms_1.capacity)

    

  


