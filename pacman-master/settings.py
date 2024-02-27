import pygame
from pathlib import Path

pygame.init()


class Settings:
    WINDOW_WIDTH = 800
    WINDOW_HEIGHT = 640
    MAX_COLLISION_COUNT = 5
    MAX_WAIT_SECONDS = 3
    BACKGROUND_COLOR = pygame.Color('black')
    scene_changed = True
    scene_index = 0
    scene_index_previous = -1

    worldWidth = 25
    worldHeight = 20
    cellSizeW = WINDOW_WIDTH // worldWidth
    cellSizeH = WINDOW_HEIGHT // worldHeight

    menumusic = pygame.mixer.Sound(Path("sounds/menu_ambient.wav"))
    gamemusic = pygame.mixer.Sound(Path("sounds/game_music.wav"))
    gameover = pygame.mixer.Sound(Path("sounds/end_of_game.wav"))

    curenttheme = menumusic

    main_effects_volume = 1

    menu_scene_volume = 0.9
    game_scene_volume = 0.2
    gameover_scene_volume = 0.4

    mv_up = pygame.K_w
    mv_left = pygame.K_a
    mv_down = pygame.K_s
    mv_right = pygame.K_d

    CONTROL_KEYS = [mv_up, mv_left, mv_down, mv_right]

    @staticmethod
    def set_scene(index, need_change_music = True, need_call_activate = False):
        if Settings.scene_index_previous != Settings.scene_index:
            Settings.scene_index_previous = Settings.scene_index
            Settings.scene_changed = need_call_activate
            Settings.scene_index = index

            if need_change_music:
                Settings.curenttheme.stop()
                if index == 0:
                    Settings.curenttheme = Settings.menumusic
                    volume = Settings.menu_scene_volume
                elif index == 1:
                    Settings.curenttheme = Settings.gamemusic
                    volume = Settings.game_scene_volume
                elif index == 3:
                    Settings.curenttheme = Settings.gameover
                    volume = Settings.gameover_scene_volume
                else:
                    volume = 0
                Settings.curenttheme.set_volume(volume)
                Settings.curenttheme.play()
            else:
                if index == 1:
                    pygame.mixer.unpause()
                elif index == 2:
                    pygame.mixer.pause()


    @staticmethod
    def new_game_scene():
        Settings.set_scene(1, True, True)

    @staticmethod
    def new_editor_scene():
        Settings.set_scene(4, True, True)

    @staticmethod
    def con_game_scene():
        Settings.set_scene(1, False, False)

    @staticmethod
    def set_menu_scene():
        Settings.set_scene(0, True, False)

    @staticmethod
    def apply_new_volume():
        volume = float(input())