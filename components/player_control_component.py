from bearlibterminal.terminal import TK_DOWN, TK_LEFT, TK_RIGHT, TK_UP


class PlayerControl:
    def __init__(self):
        self.is_up = TK_UP
        self.is_down = TK_DOWN
        self.is_right = TK_RIGHT
        self.is_left = TK_LEFT
