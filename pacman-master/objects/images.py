import pygame
from objects.base import BaseObject
from pathlib import Path


class Image(BaseObject):
    def __init__(self, filename, x, y):
        self.filename = Path(filename)
        self.image = pygame.image.load(filename).convert_alpha()
        r = self.image.get_rect()
        super().__init__(x, y, r.width, r.height)

    def draw(self, screen):
        screen.blit(self.image, self.rect)
