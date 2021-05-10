from bearlibterminal.terminal import (
    TK_CLOSE,
    TK_DOWN,
    TK_ESCAPE,
    TK_LEFT,
    TK_RIGHT,
    TK_UP,
    has_input,
    read,
)


class Controller:
    def __init__(self):
        self.is_up = False
        self.is_down = False
        self.is_right = False
        self.is_left = False
        self.is_exit = False

    def update(self):

        self.refresh_key()

        while has_input():

            key = read()

            if key == TK_UP:
                self.is_up = True

            if key == TK_DOWN:
                self.is_down = True

            if key == TK_RIGHT:
                self.is_right = True

            if key == TK_LEFT:
                self.is_left = True

            if key in {TK_ESCAPE, TK_CLOSE}:
                self.is_exit = True

    def refresh_key(self):
        self.is_up = False
        self.is_down = False
        self.is_right = False
        self.is_left = False
        self.is_exit = False
