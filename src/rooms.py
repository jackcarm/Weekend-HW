class Room:
    def __init__(self, name, price, capacity, till):
        self.name = name
        self.price = price
        self.capacity = capacity
        self.till = till
        self.guests = []
        self.song_list = []

    def guest_count(self):
        return len(self.guests)

    def add_guest(self, guests):
        self.guests.append(guests)

    def remove_guest(self, guests):
        self.guests.remove(guests)

    def song_count(self):
        return len(self.song_list)

    def add_song(self, song):
        self.song_list.append(song)

    def room_is_full(self, guests):
        if self.capacity > len(self.guests):
            self.guests.append(guests)
        return "Sorry, room is full"

    def book_room(self, guest, room):
        guest.buy_room(room)
        self.till += self.price
