from vector2 import Vector2


class TransformComponent:
    def __init__(self, vector):
        self.pos = Vector2(vector.x, vector.y)
        self.x = vector.x
        self.y = vector.y
