__author__ = 'Kellan Childers'
from tiles.tile import Tile


class Ground(Tile):
    def __init__(self, char_color="white", back_color="black"):
        super(Ground, self).__init__(".", char_color, back_color)

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character