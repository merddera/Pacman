from objects.images import Image
from settings import *
from objects.score import *

class Entity(Image):
    def __init__(self, filename, walls, position=(250, 250), velocity=1, direction=(1, 1)):
        super().__init__(filename, position[0], position[1])
        self.walls = walls

        self.velocity = velocity
        self.pos = pygame.math.Vector2(position)
        self.dir = pygame.math.Vector2(direction).normalize()

        self.now_key_x = 100
        self.previous_key_x = 100
        self.now_key_y = 115
        self.previous_key_y = 115

    def map_collisions(self, dx, dy):
        next_rect = self.rect.copy()
        next_rect.move_ip(dx, dy)
        hit_indexes = next_rect.collidelistall(self.walls)

        if len(hit_indexes):
            delta_x, delta_y = 0, 0
            for hit_index in hit_indexes:
                hit_rect = self.walls[hit_index]
                if dx > 0:
                    delta_x += next_rect.right - hit_rect.left
                else:
                    delta_x += hit_rect.right - next_rect.left
                if dy > 0:
                    delta_y += next_rect.bottom - hit_rect.top
                else:
                    delta_y += hit_rect.bottom - next_rect.top

            if abs(delta_x - delta_y) < 10:
                dx, dy = 0, 0
            elif delta_x > delta_y:
                dy = 0
            elif delta_y > delta_x:
                dx = 0
        self.rect.x += dx
        self.rect.y += dy

    def wall_collisions(self):
        if self.rect.left <= 0:
            self.reflect((1, 0))
        elif self.rect.right >= Settings.WINDOW_WIDTH:
            self.reflect((-1, 0))

        if self.rect.top <= 0:
            self.reflect((0, 1))
        elif self.rect.bottom >= Settings.WINDOW_HEIGHT:
            self.reflect((0, -1))

    def reflect(self, NV):
        self.dir = self.dir.reflect(pygame.math.Vector2(NV))

    def move(self):
        self.Row, self.Col = self.rect.y // Settings.cellSizeH, self.rect.x // Settings.cellSizeW
        self.map_collisions(self.dir.x * self.velocity, self.dir.y * self.velocity)

    def logic(self):
        self.wall_collisions()
        self.move()


class Player(Entity):
    def __init__(self, walls, seeds, position=(392, 72), velocity=1, direction=(1, 1)):
        filename = "images/pacman_right2.png"
        super().__init__(filename, walls, position, velocity, direction)

        self.points = 0
        self.seeds = seeds

    def check_keys(self, event):
        if event.type == pygame.KEYUP:
            if event.key in Settings.CONTROL_KEYS:
                if Settings.CONTROL_KEYS.index(event.key) == 1 or Settings.CONTROL_KEYS.index(event.key) == 3:
                    self.now_key_x = event.key
                    self.previous_key_x = self.now_key_x
                else:
                    self.now_key_y = event.key
                    self.previous_key_y = self.now_key_y
                self.velocity = 1
                # print(f"check_keys: {event.key}")
                self.change_move(event.key)

    def resize(self):
        self.rect.width = Settings.cellSizeW // 2
        self.rect.height = Settings.cellSizeH // 2
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))

    def change_image(self, key):
        filename = "images/pacman_right2.png"
        if Settings.CONTROL_KEYS.index(key) == 0 or Settings.CONTROL_KEYS.index(key) == 2:
            if self.previous_key_x == 97:
                filename = "images/pacman_left2.png"
        elif Settings.CONTROL_KEYS.index(key) == 1:
            filename = "images/pacman_left2.png"
        return filename

    def change_move(self, key):
        movement = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        vx, vy = movement[Settings.CONTROL_KEYS.index(key)]

        self.image = pygame.image.load(self.change_image(key))
        self.dir = pygame.math.Vector2(vx, vy).normalize()

    def wall_collisions(self):
        if self.rect.x <= -30:
            self.rect.x = Settings.WINDOW_WIDTH - 10
        elif self.rect.x >= Settings.WINDOW_WIDTH + 30:
            self.rect.x = -10

        if self.rect.y <= -30:
            self.rect.y = Settings.WINDOW_HEIGHT - 10
        elif self.rect.y >= Settings.WINDOW_HEIGHT + 30:
            self.rect.y = -10
        # там падали бомбы, ангел против демона, там жёсткая бойня

    def pick(self):
        for seed in self.seeds:
            if self.rect.colliderect(seed.rect):
                self.points += seed.bonus
                self.seeds.remove(seed)

    def logic(self):
        self.resize()
        self.pick()
        super().logic()
