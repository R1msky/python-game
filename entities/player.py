from bearlibterminal.terminal import printf as terminal_printf

from entities.entity import Entity
from entities.food import Food
from entities.wall import Wall


class Player(Entity):

    def __init__(self, controller, x=40, y=10, speed=1):
        self.controller = controller
        self.x = x
        self.y = y
        self.speed = speed
        self.symbol = '@'
        self.hunger = 5
        self.is_game_over = False
        self.tmp_coords = [x, y]

    def move(self):
        self.tmp_coords = [self.x, self.y]
        if self.controller.is_up:
            self.y -= self.speed
            self.hunger -= 1

        if self.controller.is_down:
            self.y += self.speed
            self.hunger -= 1

        if self.controller.is_left:
            self.x -= self.speed
            self.hunger -= 1

        if self.controller.is_right:
            self.x += self.speed
            self.hunger -= 1

    def render(self):
        terminal_printf(self.x, self.y, self.symbol)

    def update(self):
        self.move()
        if self.hunger <= 0:
            self.is_game_over = True

    def collide(self, other):
        if isinstance(other, Wall):
            if other.is_visible:
                self.x = self.tmp_coords[0]
                self.y = self.tmp_coords[1]

        if isinstance(other, Food):
            if other.is_visible:
                self.hunger += 2
                other.is_visible = False
