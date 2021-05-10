from bearlibterminal.terminal import printf

from scenes.scene import Scene


class GameOver(Scene):
    x: int = 30
    y: int = 10

    def create(self):
        self.scene_name = 'OOPS, GAME OVER!'

    def render(self):
        printf(self.x, self.y, self.scene_name)

    def close(self):
        pass
