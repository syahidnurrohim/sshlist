import os, json, argparse, ast, sys, time, curses
import inquirer
from .screen import Screen

class SSHList:

    def __init__(self):
        self.base_path = '/usr/share/SSHList'
        self.source = '{}/list'.format(self.base_path)

    def init_screen(self):
        stdscr = curses.initscr()
        self.frags = Screen(stdscr)
        self.screen = stdscr

    def prepare(self):
        os.makedirs(self.base_path, exist_ok=True)
        if (os.path.isfile(self.source) == False):
            open(self.source, 'a').close()
        
        self.data = self.parsedata()

    def store(self):
        cred_name = input('Name Credentials: ')
        print("Copy and Paste to end Press Ctrl+d on Linux/Mac on Crtl+z on Windows to save:")
        lines = []

        try:
            while True:
                lines.append(input())
        except EOFError:
            pass

        lines = "\n".join(lines)

        if (cred_name in self.data):
            print("Nama tersebut telah digunakan!\n")
            sys.exit(2)
        
        self.data[cred_name] = lines
        self.write()

    def find(self):
        self.init_screen()
        self.frags.panel()
        #curses.echo()
        #self.screen.clear()
        #self.frags.input('Message')
        key = ''

        while key != ord('q'):
            key = self.screen.getch()
            self.screen.refresh()
            #if c == curses.KEY_ENTER or c == 10 or c == 13:
                #curses.nl()

        curses.endwin()

    def list(self):
        prompted = inquirer.list_input('Credentials List', choices=[d for d in self.data])
        print(self.data.get(prompted))

    def get(self, name):
        data = self.data.get(name)
        if (data):
            print (data)
        else:
            print ('Tidak ditemukan informasi dengan nama {}'.format(name))

    def delete(self, name):
        data = self.data.get(name)
        if (data != None):
            del self.data[name]
            self.write()
        else:
            print('Tidak ditemukan informasi dengan nama {}'.format(name))

    def parsedata(self):
        ret = {}
        with open(self.source, "r") as f:
            data = f.read()
            if (data != ''):
                ret = json.loads(data)
            f.close()

        return ret

    def write(self):
        with open(self.source, "w") as f:
            f.write(json.dumps(self.data))
            f.close()

        


def main():
    ssh = SSHList()
    ssh.prepare()

    parser = argparse.ArgumentParser()
    parser.add_argument('--store', '-s', action='store_true')
    parser.add_argument('--list', '-l', action='store_true')
    parser.add_argument('--delete', '-d')
    parser.add_argument('--get', '-g')
    parser.add_argument('--find', '-f', action='store_true')
    args = parser.parse_args()

    for d in vars(args):
        val = vars(args)[d]
        if type(val) is bool:
            if (val): 
                getattr(ssh, d)()
        else:
            if (val != None):
                getattr(ssh, d)(val)


if __name__ == '__main__':
    main()
