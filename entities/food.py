from bearlibterminal.terminal import printf

from entities.entity import Entity


class Food(Entity):

    def __init__(self, x, y, symbol='o'):
        self.x = x
        self.y = y
        self.symbol = symbol

    def render(self):
        printf(self.x, self.y, self.symbol)
