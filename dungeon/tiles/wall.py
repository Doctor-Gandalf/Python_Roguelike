from dungeon.tiles import Tile
__author__ = 'Kellan Childers'


class Wall(Tile):
    def __init__(self, character='#', char_color="white", back_color="black"):
        super(Wall, self).__init__(character, char_color, back_color)

    def __str__(self):
        return self.character

    def __repr__(self):
        return self.character
