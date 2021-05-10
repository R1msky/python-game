from entities.food import Food
from entities.player import Player
from entities.ui.hunger import Hunger
from entities.wall import Wall
from scenes.scene import Scene
from systems.collision_system import Collider
from systems.rendering_system import Render
from systems.updater import Updater


class GameScene(Scene):

    def __init__(self, context, controller):
        self.context = context
        self.controller = controller
        self.player = None
        self.hunger = 5
        self.updater = None
        self.collider = None
        self.render = None

    def create(self):
        self.player = Player(self.controller)
        self.hunger = Hunger(self.player)

        wall_x = 38
        wall_y = [10, 11, 12]

        walls = [
            Wall(wall_x, wall_y[0]),
            Wall(wall_x, wall_y[1]),
            Wall(wall_x, wall_y[2]),
        ]

        food_x = [43, 43, 40]
        food_y = [10, 12, 12]

        food_list = [
            Food(food_x[0], food_y[0]),
            Food(food_x[1], food_y[1]),
            Food(food_x[2], food_y[2]),
        ]

        entities = [
            self.player,
            self.hunger,
        ]

        entities.extend(food_list)
        entities.extend(walls)

        self.updater = Updater(entities)
        self.collider = Collider(entities)
        self.render = Render(entities)

    def render(self):
        if self.player.is_game_over:
            self.context.set_context('game_over')
            return

        self.update()
        self.collider.update()
        self.render.update()

    def close(self):
        del self.controller
        del self.player
        del self.hunger
        del self.updater
        del self.collider
        del self.render
