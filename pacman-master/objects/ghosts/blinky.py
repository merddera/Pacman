from objects.entity import Entity
from settings import *
import random


class BlinkyGhost(Entity):
    def __init__(self, map, position=(384, 352), velocity=1, direction=(0, -1)):
        filename = "images/monster1_left1.png"
        super().__init__(filename, map, position, velocity, direction)

    def move(self):
        super().move()
        
        directions = [[0, -1], [-1, 0], [0, 1], [1, 0]] # 0-вверх 1-влево 2-вниз 3-вправо
        clear_directions = []
        revers = [int(self.dir.x) * -1, int(self.dir.y) * -1]
        
        for i in range(len(directions)):
            if directions[i] != revers:
                x, y = directions[i]

                near_rect = self.rect.copy()
                near_rect.move_ip(x * self.velocity, y * self.velocity)
                hit_indexes = near_rect.collidelistall(self.walls)

                if hit_indexes == []:
                    clear_directions.append([x, y])

        if len(clear_directions) > 0:
            num_dir = random.randint(0, len(clear_directions) - 1)

            a, b = clear_directions[num_dir]
            self.dir = pygame.math.Vector2(a, b).normalize()
        
        else:
            a, b = revers
            self.dir = pygame.math.Vector2(a, b).normalize()


    def scatter(self):
        pass

    def chase(self):
        pass
