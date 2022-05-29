class Guest:
    def __init__(self, name, wallet):
        self.name = name
        self.wallet = wallet

    def buy_room(self, room):
        self.wallet -= room.price
