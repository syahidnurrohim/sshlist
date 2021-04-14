import curses
from curses import panel

class Win():

    def __init__(self, screen):
        self.x = 0
        self.y = 1
        self.screen = screen
        curses.use_default_colors()
        curses.init_pair(1, curses.COLOR_YELLOW, -1)
        curses.init_pair(2, curses.COLOR_WHITE, -1)

    def draw(self):
        self.win = self.screen.subpad(self.y, self.x)

class LeftWin(Win):

    def __init__(self, screen):
        super().__init__(screen)
        self.x = 1
        self.position = self.y

    def draw(self, items = [[]]):
        self.items = items
        self.selected_item = items[0][0]
        super().draw()
        self.navigate(0)

    def start(self):
        self.win.addstr(20, 0, 'ENTERED START {}'.format(self.selected_item))

    def draw_menu(self):
        self.selected_item = self.items[self.position-self.y][0]
        for i, d in enumerate(self.items):
            mode = curses.A_REVERSE if i == self.position-self.y else curses.A_NORMAL
            self.win.addstr(i, self.x, '{}. {}'.format(i+1, d[0]), mode)
    
    def navigate(self, direction):
        self.position += direction
        if self.position-self.y < 0 : self.position = self.y
        if self.position-self.y > len(self.items)-1 : self.position = len(self.items)-1+self.y

        self.draw_menu()
        self.screen.move(self.position, self.x)

    def listen(self, key):
        if key == curses.KEY_DOWN: self.navigate(1)
        elif key == curses.KEY_UP: self.navigate(-1)
        elif key in [curses.KEY_ENTER, ord('\n')]: self.items[self.position][1]()



class RightWin(Win):

    def __init__(self, screen):
        super().__init__(screen)

    def draw(self):
        self.x = int(curses.COLS/5)
        super().draw()
        self.win.border(0)

    def draw_info(self, text):
        self.win.clear()
        inf = 'Information:'
        self.win.addstr(0, 0, inf, curses.color_pair(1))
        self.win.addstr(1, 0, '-'*((curses.COLS-self.x)-2), curses.A_BOLD)
        for i, d in enumerate(text.split('\n')):
            self.win.addstr(i+2, 0, "[+] {}".format(d), curses.color_pair(2))


class Separator(Win):
    def __init__(self, screen):
        super().__init__(screen)

    def draw(self, x):
        self.win = self.screen.subwin(curses.LINES, 1, 0, x)
        self.win.border(0)

class Attributes(Win):

    def __init__(self, screen):
        super().__init__(screen)

    def draw(self):
        self.screen.addstr(curses.LINES-2, 2, 'Press q to Exit')

        

