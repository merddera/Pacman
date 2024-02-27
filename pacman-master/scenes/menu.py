import pygame
from objects.buttons import Button
from objects.texts import Text
from scenes.base import BaseScene
from settings import Settings
from objects.images import Image


class MenuScene(BaseScene):
    PROCESS_ESCAPE = False
    speed = 2

    def __init__(self):
        self.playsound = pygame.mixer.Sound("sounds/start_button_click.wav")
        self.directions = 'right'
        super().__init__()

    def set_up_objects(self):
        self.objects.append(
            Image("images/menu_bckgr.png", Settings.WINDOW_WIDTH // 50, Settings.WINDOW_HEIGHT // 50 + 100))

        self.objects.append(
            Image("images/logo1.png", Settings.WINDOW_WIDTH // 50 + 94, Settings.WINDOW_HEIGHT // 50 + 170))

        self.objects.append(
            Image("images/Background_monsters.png", Settings.WINDOW_WIDTH - 230, Settings.WINDOW_HEIGHT // 140 - 5))

        self.objects.append(Image("images/pacman_right2.png", -32, Settings.WINDOW_HEIGHT - 50))

        self.objects.append(Image("images/monster3_right1.png", -64, Settings.WINDOW_HEIGHT - 50))

        self.objects.append(Button(Settings.WINDOW_WIDTH // 8, Settings.WINDOW_HEIGHT // 3 + 70, 100, 40, "Начать игру",
                                   Settings.new_game_scene))
        self.objects.append(Image("images/pacman_left2.png", 832, Settings.WINDOW_HEIGHT - 50))

        self.objects.append(Image("images/monster1_left1.png", 864, Settings.WINDOW_HEIGHT - 50))

        self.objects.append(
            Button(Settings.WINDOW_WIDTH // 8, (Settings.WINDOW_HEIGHT // 3) + 140, 100, 40, "Настройка карты",
                   Settings.new_editor_scene))

        self.objects.append(
            Button(Settings.WINDOW_WIDTH // 8, (Settings.WINDOW_HEIGHT // 3) + 210, 100, 40, "Выйти из игры", exit))

    def activate(self):
        super().activate()

    def process_event(self, event):
        super().process_event(event)

        if self.objects[5].internal_button.clicked:
            self.playsound.play()
            pygame.mixer.music.pause()

    def process_logic(self):
        super().process_logic()
        if self.directions == 'right':
            self.objects[4].rect.x += 1
            self.objects[3].rect.x += 1.5

            if self.objects[4].rect.x >= 864 and self.objects[3].rect.x >= 864:
                self.objects[4].rect.x = -64
                self.objects[3].rect.x = -32
                self.directions = 'left'

        if self.directions == 'left':
            self.objects[7].rect.x -= 1
            self.objects[6].rect.x -= 2

            if self.objects[7].rect.x <= -64 and self.objects[6].rect.x <= -64:
                self.objects[6].rect.x = 832
                self.objects[7].rect.x = 864
                self.directions = 'right'

    def process_draw(self, screen):
        super().process_draw(screen)
