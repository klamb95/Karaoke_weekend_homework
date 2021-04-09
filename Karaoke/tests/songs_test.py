import unittest
from src.songs import Songs

class TestSongs(unittest.TestCase):

    def setUp(self):
        self.songs = Songs("Dive", "Ed Sheeran")


    def test_songs_has_title(self):
        self.assertEqual("Dive", self.songs.title)