from vector2 import Vector2


class MovementComponent:
    def __init__(self, direction, speed=1,):
        self.speed = speed
        self.direction = direction
