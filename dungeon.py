__author__ = 'Kellan Childers'
from graph import Graph
from tiles.tile import Tile


class Dungeon(Graph):
    def __init__(self, x=10, y=10, default=Tile(' ')):
        super(Dungeon, self).__init__(x, y, default)

    def make_rectangle(self, x_start, x_end, y_start, y_end, line_element=Tile("#")):
        self.make_line(range(x_start, x_end+1), [y_start for _ in range(x_start, x_end+1)], line_element)
        self.make_line(range(x_start, x_end+1), [y_end for _ in range(x_start, x_end+1)], line_element)
        self.make_line([x_start for _ in range(y_start, y_end+1)], range(y_start, y_end+1), line_element)
        self.make_line([x_end for _ in range(y_start, y_end+1)], range(y_start, y_end+1), line_element)

    def make_line(self, x_list, y_list, line_element=Tile("#")):
        for x, y in zip(x_list, y_list):
            if 0 <= y < self.get_height() and 0 <= x < self.get_width():
                self.set_elem(line_element, x, y)
            else:
                continue

if __name__ == "__main__":
    test_dungeon = Dungeon(80, 12)
    test_dungeon.make_rectangle(0, 79, 0, 11, Tile("."))
    test_dungeon.print_all()
