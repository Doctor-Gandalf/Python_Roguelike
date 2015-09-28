__author__ = 'Kellan Childers'


class Tile:
    def __init__(self, character, char_color="white", back_color="black"):
        self.character = character
        self.char_color = char_color
        self.back_color = back_color

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character
