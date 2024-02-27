import pygame
from objects.texts import Text
from scenes.base import BaseScene
from settings import Settings
from objects.images import Image
from objects.buttons import Button


class GameoverScene(BaseScene):
    def __init__(self):
        super().__init__()

    def set_up_objects(self):
        self.objects.append(Image("images/gameover.png", Settings.WINDOW_WIDTH // 50,
                                  Settings.WINDOW_HEIGHT // 50 + 100))

        self.objects.append(Button(Settings.WINDOW_WIDTH // 2 - 100, Settings.WINDOW_HEIGHT // 2, 100, 40,
                                   "Главное меню", Settings.set_menu_scene))

        self.objects.append(Button(Settings.WINDOW_WIDTH // 2, Settings.WINDOW_HEIGHT // 2, 100, 40, "Начать заново",
                                   Settings.new_game_scene))
        
        self.objects.append(Button(Settings.WINDOW_WIDTH // 2 + 100, Settings.WINDOW_HEIGHT // 2, 100, 40,
                                   "Выйти из игры", exit))

    def activate(self):
        super().activate()
        #points = random.randint(10, 100)
        #GameScene.objects[5].recreate_text("очки: " + str(points))

    def process_event(self, event):
        super().process_event(event)

    def process_logic(self):
        super().process_logic()

    def process_draw(self, screen):
        super().process_draw(screen)
