from dungeon.dungeon import Dungeon
__author__ = 'Kellan Childers'


class DungeonView:
    def __init__(self, width=10, height=10):
        self.dungeon = Dungeon(width, height)
        # Implement view as a pad
