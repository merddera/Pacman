import pygame
from objects.texts import Text
from scenes.base import BaseScene
from settings import Settings
from objects.images import Image
from objects.buttons import Button


class PauseScene(BaseScene):
    def __init__(self):
        super().__init__()

    def set_up_objects(self):
        self.objects.append(
            Image("images/pause.png", Settings.WINDOW_WIDTH - 450, Settings.WINDOW_HEIGHT - 430))

        self.objects.append(
            Image("images/logo2.png", Settings.WINDOW_WIDTH // 50 + 90, Settings.WINDOW_HEIGHT // 50 + 170))

        self.objects.append(Button(Settings.WINDOW_WIDTH // 8, Settings.WINDOW_HEIGHT // 3 + 70, 100, 40, "Продолжить",
                                   Settings.con_game_scene))

        self.objects.append(Button(Settings.WINDOW_WIDTH // 8, (Settings.WINDOW_HEIGHT // 3) + 140, 100, 40, "Начать заново",
                                   Settings.new_game_scene))

        self.objects.append(Button(Settings.WINDOW_WIDTH // 8, (Settings.WINDOW_HEIGHT // 3) + 210, 100, 40,
                                   "Главное меню", Settings.set_menu_scene))

    def activate(self):
        super().activate()

    def process_event(self, event):
        super().process_event(event)

    def process_logic(self):
        super().process_logic()

    def process_draw(self, screen):
        super().process_draw(screen)
