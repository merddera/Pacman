import pygame
from objects.base import BaseObject
from third_party.button import Button as InternalButton


class Button(BaseObject):
    BUTTON_STYLE = {
        "hover_color": pygame.Color('yellow'),
        "clicked_color": pygame.Color('dark gray'),
        "clicked_font_color": pygame.Color('white'),
        "hover_font_color": pygame.Color('black'),
    }

    def __init__(self, x, y, width, height, title, action):
        super(Button, self).__init__(x, y, width, height)
        self.internal_button = InternalButton(self.rect, pygame.Color('black'), action, text=title, **self.BUTTON_STYLE)

    def event(self, event: pygame.event.Event) -> None:
        self.internal_button.check_event(event)

    def draw(self, screen: pygame.Surface) -> None:
        self.internal_button.update(screen)
