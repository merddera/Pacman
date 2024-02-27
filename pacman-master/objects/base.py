import pygame
from settings import *


class BaseObject(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.rect = pygame.Rect(x, y, width, height)
        self.Row, self.Col = self.rect.centery // Settings.cellSizeH, self.rect.centerx // Settings.cellSizeW

    def activate(self):
        pass

    def event(self, event):
        pass

    def move(self):
        pass

    def logic(self):
        pass

    def draw(self, screen):
        pass
