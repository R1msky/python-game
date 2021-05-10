from bearlibterminal.terminal import printf

from entities.entity import Entity


class Wall(Entity):

    def __init__(self, x, y, symbol='#'):
        self.x = x
        self.y = y
        self.symbol = symbol

    def render(self):
        printf(self.x, self.y, self.symbol)
