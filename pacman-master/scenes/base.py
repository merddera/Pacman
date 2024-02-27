import pygame
from settings import Settings


class BaseScene:
    PROCESS_ESCAPE = True

    def __init__(self):
        self.world = []
        self.objects = []
        self.set_up_objects()

    def save_map(self):
        try:
            file = open('map.txt', 'w')
            for row in range(Settings.worldHeight):
                for col in range(Settings.worldWidth):
                    print(self.world[row][col], file=file, end="")
                print(file=file)
        except Exception as e:
            print(e)
        finally:
            file.close()
        print("save")

    def load_map(self, reload=False):
        try:
            if not reload:
                file = open('map.txt', 'r')
            else:
                file = open('default.txt', 'r')
            for i, line in enumerate(file):
                line = line.replace("\n", "")
                for s in range(len(line)):
                    self.world[i][s] = int(line[s])
        except Exception as e:
            print(e)
        finally:
            file.close()

    def set_up_objects(self):
        pass

    def activate(self):
        for item in self.objects:
            item.activate()
        self.additional_activate()

    def additional_activate(self):
        pass

    def process_escape_event(self, event):
        if not self.PROCESS_ESCAPE:
            return
        if event.type != pygame.KEYDOWN or event.key != pygame.K_ESCAPE:
            return
        Settings.set_scene(0)

    def process_event(self, event):
        for item in self.objects:
            item.event(event)
        self.additional_process_event(event)
        self.process_escape_event(event)

    def additional_process_event(self, event):
        if event.type == pygame.KEYDOWN and event.key == pygame.K_p:
            if Settings.scene_index == 1:
                Settings.set_scene(2, 0)
            elif Settings.scene_index == 2:
                Settings.set_scene(1, 0)

    def process_logic(self):
        for item in self.objects:
            item.logic()
        self.process_additional_logic()

    def process_additional_logic(self):
        pass

    def process_draw(self, screen):
        for item in self.objects:
            item.draw(screen)
        self.process_additional_draw(screen)

    def process_additional_draw(self, screen):
        pass
