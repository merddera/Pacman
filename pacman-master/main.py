import os
import shutil
from settings import *
from application import Application


def main():
    pygame.init()
    pygame.font.init()
    pygame.display.set_caption('PACMAN')
    pygame.display.set_icon(pygame.image.load('images/pacman_right2.png'))
    Settings.curenttheme.set_volume(Settings.menu_scene_volume)
    Settings.curenttheme.play()

    screen = pygame.display.set_mode([Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT])

    if not os.path.isfile('map.txt'):
        shutil.copyfile('default.txt', 'map.txt')

    app = Application(screen)
    app.run()

    exit(0)


if __name__ == '__main__':
    main()
