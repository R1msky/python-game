from bearlibterminal import terminal

from systems.system import System


class Render(System):

    def update(self):
        terminal.clear()

        for e in self.entities:
            if e.is_visible:
                e.render()

        terminal.refresh()
