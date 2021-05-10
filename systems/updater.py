from systems.system import System


class Updater(System):

    def update(self):
        for e in self.entities:
            e.update()
