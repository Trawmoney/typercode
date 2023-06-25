import random
import time
from typing import List
from terminal_window import TerminalWindow

class Game:
    def __init__(self):
        self.window = TerminalWindow()
        self.score = 0
        self.start_time = None
        self.words_typed = 0
        self.total_words = 0
        self.text = ""
        self.user_input = ""

    def start_game(self):
        self.start_time = time.time()
        self.text = self.generate_text()
        self.window.draw_text(self.text)

        while True:
            self.user_input = self.window.get_input()
            self.check_input()
            self.window.draw_input(self.user_input)
            self.window.update_display()

            if self.words_typed == self.total_words:
                self.update_score()
                self.window.draw_score(self.score)
                break

    def update_score(self):
        elapsed_time = time.time() - self.start_time
        wpm = (self.words_typed / elapsed_time) * 60
        accuracy = self.words_typed / self.total_words
        self.score = int(wpm * accuracy)

    def generate_text(self) -> List[str]:
        # Add more programming functions as needed
        functions = ["print()", "for i in range()", "if x == y:", "def func():", "return x + y"]
        text = random.sample(functions, len(functions))
        self.total_words = len(text)
        return " ".join(text)

    def check_input(self):
        if self.user_input == self.text[:len(self.user_input)]:
            if self.user_input[-1] == " ":
                self.words_typed += 1
        else:
            self.user_input = self.user_input[:-1]

if __name__ == "__main__":
    game = Game()
    game.start_game()
