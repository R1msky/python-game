from bearlibterminal import terminal

from engine.controller import Controller
from entities.food import Food
from entities.player import Player
from entities.ui.hunger import Hunger
from entities.wall import Wall
from systems.collision_system import Collider
from systems.rendering_system import Render
from systems.updater import Updater

GMOVR_X = 30
GMOVR_Y = 10

WALL_X = 38
WALL_Y = (10, 11, 12)

FOOD_X = (43, 43, 40)
FOOD_Y = (10, 12, 12)


def main():
    terminal.open()
    terminal.refresh()

    controller = Controller()
    player = Player(controller)
    hunger = Hunger(player)

    walls = [
        Wall(WALL_X, WALL_Y[0]),
        Wall(WALL_X, WALL_Y[1]),
        Wall(WALL_X, WALL_Y[2]),
    ]

    food_list = [
        Food(FOOD_X[0], FOOD_Y[0]),
        Food(FOOD_X[1], FOOD_Y[1]),
        Food(FOOD_X[2], FOOD_Y[2]),
    ]

    entities = [
        player,
        hunger,
    ]

    entities.extend(food_list)
    entities.extend(walls)

    updater = Updater(entities)
    collider = Collider(entities)
    render = Render(entities)

    while True:

        controller.update()

        if controller.is_exit:
            break

        if player.is_game_over:
            render_game_over()
        else:
            terminal.refresh()

            updater.update()
            collider.update()
            render.update()

    terminal.close()


def render_game_over():
    terminal.clear()
    terminal.printf(GMOVR_X, GMOVR_Y, 'OOPS, GAME OVER!')
    terminal.refresh()


if __name__ == '__main__':
    main()
