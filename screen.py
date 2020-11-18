import curses
from curses import panel

class Screen():
    def __init__(self, screen):
        self.screen = screen

    def input(self, message, x = 0, y = 0):
        char_len = len(message)
        self.screen.addstr(y, x, 'Input: ')
        self.screen.refresh()
        return self.screen.getstr(y, char_len, 60)
