from math import hypot


class Vector2:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vector2D({}, {})'.format(self.x, self.y)

    def __str__(self):
        return '({}, {})'.format(self.x, self.y)

    def __add__(self, other):
        return Vector2(self.x + other.x, self.y + other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return self

    def __mul__(self, other):
        return Vector2(self.x * other.x, self.y * other.y)

    def __imul__(self, other):
        self.x *= other.x
        self.y *= other.y
        return self

    def __mul__(self, const):
        return Vector2(self.x * const, self.y * const)

    def __imul__(self, const):
        self.x *= const
        self.y *= const
        return self

    def __sub__(self, other):
        return Vector2(self.x - other.x, self.y - other.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return self

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return self.x != 0 or self.y != 0

    def __neg__(self):
        return Vector2(-self.x, -self.y)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    @staticmethod
    def up_vec2():
        return Vector2(0, 1)

    @staticmethod
    def down_vec2():
        return Vector2(0, -1)

    @staticmethod
    def right_vec2():
        return Vector2(1, 0)

    @staticmethod
    def left_vec2():
        return Vector2(-1, 0)

    @staticmethod
    def zero_vec2():
        return Vector2(0, 0)

    @staticmethod
    def unit_vec2():
        return Vector2(1, 1)
