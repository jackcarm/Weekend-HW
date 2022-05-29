import unittest

from src.songs import Song


class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("No One Knows")

    def test_has_song(self):
        self.assertEqual("No One Knows", self.song.song)
