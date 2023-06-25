import curses

class TerminalWindow:
    def __init__(self):
        self.stdscr = curses.initscr()
        curses.noecho()
        curses.cbreak()
        self.stdscr.keypad(True)
        self.stdscr.timeout(100)

    def __del__(self):
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def draw_text(self, text: str):
        self.stdscr.addstr(1, 1, text)

    def draw_input(self, user_input: str):
        self.stdscr.addstr(3, 1, user_input)

    def draw_score(self, score: int):
        self.stdscr.addstr(5, 1, f"Score: {score}")

    def update_display(self):
        self.stdscr.refresh()

    def get_input(self) -> str:
        return self.stdscr.getstr(3, 1).decode("utf-8")
