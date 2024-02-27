from scenes.base import BaseScene
from objects.entity import *
from objects.ghosts.blinky import *
from objects.ghosts.clyde import *
from objects.ghosts.inky import *
from objects.ghosts.pinky import *
from objects.field import *
from objects.score import *
from settings import Settings


class GameScene(BaseScene):
    def __init__(self):
        super().__init__()
        self.flag = True
        self.field = Field(self.objects, self.world)
        #self.pointdrawer = PointDrawer(Settings.WINDOW_WIDTH // 3, 498, "очки: ", 37, (255, 255, 0))

    def interaction(self):
        for i in self.objects:
            if type(i) != Player and type(i) != Field:
                status = i.rect.colliderect(self.pacman)
                if status and self.flag:
                    Settings.set_scene(3)
                    self.flag = False

    def set_up_objects(self):
        self.flag = True

        self.world = []
        for row in range(Settings.worldHeight):
            line = []
            for col in range(Settings.worldWidth):
                line.append(0)
            self.world.append(line)
        self.load_map()
        self.field = Field(self.objects, self.world)
        # очень важно чтобы поле заинициализировалось после прогрузки

        self.objects = []

        self.pacman = Player(self.field.walls, self.field.seeds)
        self.blinky = BlinkyGhost(self.field.walls)
        self.clyde = ClydeGhost(self.field.walls)
        self.inky = InkyGhost(self.field.walls)
        self.pinky = PinkyGhost(self.field.walls)

        self.objects.append(self.pacman)
        self.objects.append(self.blinky)
        self.objects.append(self.clyde)
        self.objects.append(self.inky)
        self.objects.append(self.pinky)

        #self.objects.append(point_drawer(Settings.WINDOW_WIDTH // 3, 498, "очки: ", 37, (255, 255, 0)))
        self.objects.append(self.field)
        # важно чтобы поле было последним

    def activate(self):
        self.set_up_objects()
        super().activate()

    def process_event(self, event):
        self.pacman.check_keys(event)
        super().process_event(event)

    def process_logic(self):
        super().process_logic()
        self.interaction()

    def process_draw(self, screen):
        super().process_draw(screen)
        #self.pointdrawer.points = self.pacman.points
        #self.pointdrawer.draw(screen)
