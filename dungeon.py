__author__ = 'Kellan Childers'
from graph import Graph
from tiles import *


class Dungeon(Graph):
    def __init__(self, x=10, y=10, default=Ground()):
        """Construct a dungeon of given width and height.

        :param x: the width (x-axis) for the new dungeon (default 10)
        :param y: the height (y-axis) for the new dungeon (default 10)
        :param default: the default value for each element in the graph (default ground tile)
        :type default: Tile
        :return: null
        """
        super(Dungeon, self).__init__(x, y, default)

    def make_rectangle(self, x_start, y_start, x_end, y_end, line_element=Wall()):
        """Add a rectangle of tiles to the dungeon.

        :param x_start: the x-element of the start point of the rectangle (bottom left)
        :param y_start: the y-element of the start point of the rectangle (bottom left)
        :param x_end: the x-element of the end point of the rectangle (top right)
        :param y_end: the y-element of the end point of the rectangle (top right)
        :param line_element: the type of tile to be added in the rectangle (default wall tile)
        :type line_element: Tile
        :return: null
        """
        self.make_line([(x, y_start) for x in range(x_start, x_end+1)], line_element)
        self.make_line([(x, y_end) for x in range(x_start, x_end+1)], line_element)
        self.make_line([(x_start, y) for y in range(y_start, y_end+1)], line_element)
        self.make_line([(x_end, y) for y in range(y_start, y_end+1)], line_element)

    def make_line(self, point_list, line_element=Wall()):
        """Add a line of tiles along a set of points to the dungeon.

        :param point_list: the list of points in the form (x, y)
        :param line_element: the type of tile to be added in the rectangle (default wall tile)
        :type line_element: Tile
        :return: null
        """
        for x, y in point_list:
            if 0 <= y < self.get_height() and 0 <= x < self.get_width():
                self.set_elem(line_element, x, y)
            else:
                continue

if __name__ == "__main__":
    test_dungeon = Dungeon(80, 12)
    test_dungeon.make_rectangle(0, 0, 79, 11)
    test_dungeon.make_line([(x+39, y+5) for x in range(-1, 2) for y in range(-1, 2) if x**2 + y**2 == 1])
    test_dungeon.print_all()
