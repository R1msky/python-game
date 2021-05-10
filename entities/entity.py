class Entity:
    x: int = 0
    y: int = 0

    is_visible: bool = True
    is_wall: bool = False

    def update(self):
        pass

    def render(self):
        pass

    def collide(self, other_entity):
        pass
