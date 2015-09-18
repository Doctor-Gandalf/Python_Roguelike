__author__ = 'Kellan Childers'

import curses
import curses_helper.util as util
from dungeon import Dungeon


class MainScreen:
    def __init__(self, console_height, console_width):
        """Create a main screen.

        :param console_height: the height of the console
        :param console_width: the width of the console
        :return: null
        """
        # List should be two smaller in each direction because of surrounding border.
        self._dungeon_height, self._dungeon_width = console_height-2, console_width-2

        # Center the window based on the size of the console.
        display_start_y, display_start_x = util.center_start(console_height, console_width,
                                                             self._dungeon_height, self._dungeon_width)

        # Initialize a Dungeon to serve as a main dungeon.
        self._dungeon = Dungeon(self._dungeon_width, self._dungeon_height)

        # Create window that will act as main visual.
        self._dungeon_display = curses.newwin(self._dungeon_height, self._dungeon_width, display_start_y, display_start_x)

        # Add visual detail to window.
        self._dungeon_display.bkgd(' ', curses.color_pair(1))
        util.color_box(self._dungeon_display, 0, 0, self._dungeon_height-1, self._dungeon_width-1, 3)

        # Initializes help window for use in pause().
        help_height, help_width = 12, 50
        help_y, help_x = util.center_start(console_height, console_width, help_height, help_width)
        self.help_window = curses.newwin(help_height, help_width, help_y, help_x)

    def request_element(self, request):
        """Ask for an element.

        :param request: the request for the element (requires string)
        :return: the user's response
        """
        # Clear row in preparation of getting element.
        self._dungeon_display.addstr(self._dungeon_height-2, 1, ' '*(self._dungeon_width-2))

        # Format request, then request.
        _, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, len(request))
        self._dungeon_display.addstr(self._dungeon_height-2, line_x, request)
        self._dungeon_display.refresh()

        # Get element.
        curses.echo()
        element = self._dungeon_display.getstr().decode(encoding="utf-8")
        curses.noecho()

        return element

    def start_load(self):
        """Loads a list from a file.

        :return: null
        """
        # Request filename.
        line_y, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 16)
        self._dungeon_display.addstr(line_y+4, 1, ' '*(self._dungeon_width-2))
        self._dungeon_display.addstr(line_y+4, line_x, "Enter filename: ")
        self._dungeon_display.refresh()

        # Get filename
        curses.echo()
        filename = self._dungeon_display.getstr().decode(encoding="utf-8")
        filename = 'shopping_lists/data/' + filename
        curses.noecho()

        # Try to load list, and recursively call start_command if the file isn't loaded.
        try:
            # new_list = Recipe.create_from_file(filename)
            # Add ingredients to the shopping list.
            # new_list.add_to(self._shopping_list)

            # Alert user that list was updated..
            line_y, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, len(filename)+13)
            self._dungeon_display.addstr(line_y+5, line_x, "{} fully loaded".format(filename))
            self._dungeon_display.refresh()
        except (FileNotFoundError, IsADirectoryError):
            # Alert user that file was not found.
            line_y, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 13)
            self._dungeon_display.addstr(line_y+5, line_x, "File not found.")
            self._dungeon_display.refresh()

            # Retry getting a command
            self.start_shopping_list()

    def show_intro(self):
        """Show welcome text."""
        # Calling util.center_start using the length of the string will center the string.
        # Line length acquired by adding str(len(...)) around text and running program.
        line_1_y, line_1_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 18)
        self._dungeon_display.addstr(line_1_y, line_1_x, "Welcome to RecAppE")

        line_2_y, line_2_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 42)
        self._dungeon_display.addstr(line_2_y+1, line_2_x, "To create a new shopping list, press enter")

        line_3_y, line_3_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 52)
        self._dungeon_display.addstr(line_3_y+2, line_3_x, "To add to a previously made shopping list, press 'l'")

        line_4_y, line_4_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 30)
        self._dungeon_display.addstr(line_4_y+3, line_4_x, "To quit, press 'q' at any time")

        self._dungeon_display.refresh()

    def start_shopping_list(self):
        """Start the main screen by getting a command from a key.

        Pressing 'q' will quit app.
        :return: a reference to the main screen
        """
        key = self._dungeon_display.getkey()
        if key == '\n':
            # Shopping list is already empty so program can continue
            return self
        elif key == 'l':
            # Load a shopping list from saves.
            self.start_load()
            return self
        elif key == 'q':
            # quit app.
            exit()
        else:
            # Use same method for centering text as show_intro(); add text below show_intro()'s.
            line_y, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 28)
            self._dungeon_display.addstr(line_y+4, line_x, "Command not found, try again")

            self._dungeon_display.refresh()
            self.start_shopping_list()

    def clear_screen(self):
        """Clear the contents of the screen.

        :return: a reference to the main screen
        """
        self._dungeon_display.clear()

        # Add back border and show display
        util.color_box(self._dungeon_display, 0, 0, self._dungeon_height-1, self._dungeon_width-1, 3)
        self._dungeon_display.refresh()

        return self

    def help(self):
        """Show help window."""
        self.help_window.bkgd(' ', curses.color_pair(0))

        self.help_window.addstr(1, 19, "Help window")
        self.help_window.addstr(3, 12, "To add an item, press 'a'")
        self.help_window.addstr(4, 11, "To remove an item, press 'r'")
        self.help_window.addstr(5, 11, "To load a recipe, press 'l'")
        self.help_window.addstr(6, 10, "To save as a recipe, press 'w'")
        self.help_window.addstr(7, 6, "To save as a shopping list, press 's'")
        self.help_window.addstr(8, 12, "To clear the list, press 'c'")
        self.help_window.addstr(9, 16, "To quit, press 'q'")
        self.help_window.addstr(10, 3, "Otherwise, press 'h' to return to application")

        self.help_window.refresh()

        # Close if user hits 'h', otherwise do the command user asks.
        key = self.help_window.getkey()
        if key == 'h':
            return
        else:
            self.do_command(key)

    def do_command(self, key=None):
        """Execute a command based on key input."""
        if key is None:
            key = self._dungeon_display.getkey()

        # Clear line in case a previous command had written to it.
        self._dungeon_display.addstr(self._dungeon_height-2, 1, ' '*(self._dungeon_width-2))
        self._dungeon_display.refresh()

        if key == 'l':
            # Load a recipe.
            try:
                filename = self.request_element("Enter name of recipe to load: ")
                self.add_recipe(filename)
            except (FileNotFoundError, IsADirectoryError):
                # Alert user that recipe wasn't loaded.
                _, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 18)
                self._dungeon_display.addstr(self._dungeon_height-2, 1, ' '*(self._dungeon_width-2))
                self._dungeon_display.addstr(self._dungeon_height-2, line_x, "File not found")
                self._dungeon_display.refresh()
                self.do_command()
        elif key == 'a':
            # Add an ingredient.
            try:
                # Pull data to add as a new ingredient.
                item_name = self.request_element("Enter name of item: ")
                item_quantity = int(self.request_element("Enter quantity of item: "))
                item_qualifier = self.request_element("Enter qualifier of item: ")

                self.add_item(item_name, item_quantity, item_qualifier)
            except ValueError:
                self._dungeon_display.addstr(self._dungeon_height-2, 1, ' '*(self._dungeon_width-2))
                _, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 18)
                self._dungeon_display.addstr(self._dungeon_height-2, line_x, "Could not add item")
                self._dungeon_display.refresh()
                self.do_command()
        elif key == 'q':
            # Quit app.
            exit()
        elif key == 's':
            # Save shopping list.
            try:
                filename = self.request_element("Enter name to save list as: ")
                self.save_list(filename)
            except IsADirectoryError:
                # User didn't enter file, so tell the user and retry.
                self._dungeon_display.addstr(self._dungeon_height-2, 1, ' '*(self._dungeon_width-2))

                _, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 23)
                self._dungeon_display.addstr(self._dungeon_height-2, line_x, "File unable to be saved")

                self._dungeon_display.refresh()
                self.do_command()
        elif key == 'w':
            # Save shopping list as a recipe.
            try:
                filename = self.request_element("Enter name to save recipe as: ")
                # self.save_as_recipe(filename)
            except IsADirectoryError:
                # User didn't enter file, so tell the user and retry.
                self._dungeon_display.addstr(self._dungeon_height-2, 1, ' '*(self._dungeon_width-2))

                _, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 23)
                self._dungeon_display.addstr(self._dungeon_height-2, line_x, "File unable to be saved")

                self._dungeon_display.refresh()
                self.do_command()
        elif key == 'c':
            # Clear the shopping list.
            # self._shopping_list.clear()
            pass
        elif key == 'r':
            # Remove item.
            try:
                item_name = self.request_element("Enter item to remove: ")
                # self.remove_item(item_name)
            except ValueError:
                # Item wasn't in list, so tell the user and retry.
                self._dungeon_display.addstr(self._dungeon_height-2, 1, ' '*(self._dungeon_width-2))

                _, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 15)
                self._dungeon_display.addstr(self._dungeon_height-2, line_x, "Item not found")

                self._dungeon_display.refresh()
                self.do_command()
        elif key == 'h':
            # Show help window
            self.help()
        else:
            # Tell the user that the key was an invalid command.
            _, line_x = util.center_start(self._dungeon_height-2, self._dungeon_width-2, 1, 18)
            self._dungeon_display.addstr(self._dungeon_height-2, line_x, "Command not found")
            self._dungeon_display.refresh()
            self.do_command()
