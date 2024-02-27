import pygame
from scenes.menu import MenuScene
from scenes.game import GameScene
from scenes.pause import PauseScene
from scenes.gameover import GameoverScene
from scenes.editor import EditorScene
from settings import Settings


class Application:
    def __init__(self, screen):
        self.screen = screen
        self.game_over = False
        self.scenes = [
            MenuScene(),
            GameScene(),
            PauseScene(),
            GameoverScene(),
            EditorScene(screen)
        ]

    def scene_activate(self):
        Settings.scene_changed = False
        self.scenes[Settings.scene_index].activate()

    def scene_event(self):
        for event in pygame.event.get():
            self.process_application_exit(event)
            self.scenes[Settings.scene_index].process_event(event)

    def process_application_exit(self, event):
        if event.type != pygame.QUIT:
            return
        self.game_over = True

    def scene_logic(self):
        self.scenes[Settings.scene_index].process_logic()

    def scene_draw(self):
        self.screen.fill(Settings.BACKGROUND_COLOR)
        self.scenes[Settings.scene_index].process_draw(self.screen)
        pygame.display.flip()

    def process_frame(self):
        if Settings.scene_changed:
            self.scene_activate()
            return
        self.scene_event()
        self.scene_logic()
        self.scene_draw()
        pygame.time.wait(3)

    def run(self):
        while not self.game_over:
            self.process_frame()
