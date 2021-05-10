from bearlibterminal.terminal import printf

from entities.entity import Entity


class Hunger(Entity):

    def __init__(self, player, x=3, y=1, text='Hunger:'):
        self.x = x
        self.y = y
        self.text = text
        self.player = player

    def render(self):
        s = f'{self.text}{self.player.hunger}'
        printf(self.x, self.y, s)
