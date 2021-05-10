from systems.system import System


class Collider(System):

    def update(self):
        n = range(len(self.entities))

        collision_matrix = self._get_collision_matrix(n)

        self._call_collide(n, collision_matrix)

    def _get_collision_matrix(self, n):
        collision_matrix = [[0 for i in n] for i in n]

        for i in n:
            for j in n:
                if (
                    i != j and
                    self.entities[i].x == self.entities[j].x and
                    self.entities[i].y == self.entities[j].y
                ):
                    collision_matrix[i][j] = 1

        return collision_matrix

    def _call_collide(self, n, collision_matrix):
        for i in n:
            for j in n:
                if collision_matrix[i][j] >= 1:
                    self.entities[i].collide(self.entities[j])
