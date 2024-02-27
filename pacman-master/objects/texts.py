import pygame
from objects.base import BaseObject


class Text(BaseObject):
    def __init__(self, x, y, text, size, color, width=0, height=0):
        super().__init__(x, y, width, height)
        self.color = color
        self.size = size
        self.text = text
        self.font = pygame.font.SysFont('Courier New', self.size, True, False)
        self.texture = None
        self.render()

    def render(self):
        self.texture = self.font.render(self.text, True, self.color)
        r = self.texture.get_rect()
        self.rect.width = r.width
        self.rect.height = r.height

    def draw(self, screen):
        screen.blit(self.texture, self.rect)


class RecalculableText(Text):
    def __init__(self, x, y, text, size, color):
        super().__init__(x, y, text, size, color)
        self.text_format = self.text

    def recreate_text(self, *args, **kwargs) -> None:
        self.text = self.text_format.format(*args, **kwargs)
        self.render()
