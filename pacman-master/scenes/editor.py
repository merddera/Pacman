from scenes.base import BaseScene
from objects.cells import *
from settings import Settings


class EditorScene(BaseScene):
    def __init__(self, screen):
        super().__init__()
        self.screen = screen

    def interaction(self):
        mousePX, mousePY = pygame.mouse.get_pos()
        b1, b2, b3 = pygame.mouse.get_pressed()

        mouseRow, mouseCol = mousePY // Settings.cellSizeH, mousePX // Settings.cellSizeW
        if b1:
            self.world[mouseRow][mouseCol] = 1
        elif b3:
            self.world[mouseRow][mouseCol] = 0

    def set_up_objects(self):
        self.world = []
        for row in range(Settings.worldHeight):
            line = []
            for col in range(Settings.worldWidth):
                line.append(0)
            self.world.append(line)

    def activate(self):
        self.set_up_objects()
        super().activate()

    def process_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_s:
            super().save_map()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_l:
            super().load_map()
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_h:
            super().load_map(True)
        super().process_event(event)

    def process_logic(self):
        super().process_logic()
        self.interaction()

    def process_draw(self, screen):
        for row in range(Settings.worldHeight):
            for col in range(Settings.worldWidth):
                x, y = col * Settings.cellSizeW, row * Settings.cellSizeH
                if self.world[row][col] == 1:
                    pygame.draw.rect(self.screen, pygame.Color('gray'), (x, y, Settings.cellSizeW, Settings.cellSizeH))
                else:
                    pygame.draw.rect(self.screen, pygame.Color('gray'), (x, y, Settings.cellSizeW, Settings.cellSizeH), 1)