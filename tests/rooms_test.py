import unittest

from src.rooms import Room
from src.songs import Song
from src.guests import Guest


class TestRoom(unittest.TestCase):
    def setUp(self):
        self.room = Room("1", 5.00, 10, 100)
        self.room_2 = Room("2", 5.00, 10, 100)
        self.song_1 = Song("No One Knows")
        self.song_2 = Song("Wipeout")
        self.guest_1 = Guest("Steven Seagal", 10.00)
        self.guest_2 = Guest("Jeremey Clarkson", 10.00)
        self.guest_3 = Guest("Harry Potter", 10.00)

    def test_has_room(self):
        self.assertEqual("1", self.room.name)

    def test_add_guest_to_room(self):
        self.room.add_guest(self.guest_1)
        self.assertEqual(1, self.room.guest_count())

    def test_remove_guest_from_room(self):
        self.room.add_guest(self.guest_2)
        self.assertEqual(1, self.room.guest_count())

    def test_add_song_to_room(self):
        self.room.add_song(self.song_1)
        self.assertEqual(1, self.room.song_count())

    def test_room_is_full(self):
        self.assertEqual("Sorry, room is full", self.room.room_is_full(self.room))

    def test_has_room_price(self):
        self.assertEqual(5, self.room.price)

    def test_does_room_have_till(self):
        self.assertEqual(100.00, self.room.till)

    def test_room_charge(self):
        self.room.add_guest(self.guest_2)
        self.room.book_room(self.guest_2, self.room)
        self.assertEqual(5, self.guest_2.wallet)
        self.assertEqual(105, self.room.till)
