import pygame
from objects.cells import Wall, Empty, UndefinedCell
from objects.base import BaseObject
from settings import Settings
from objects.seeds import *


class Field(BaseObject):
    """A class for containing and processing arrays of cell objects"""

    def __init__(self, objects, level: str or list[list[int]], mapping: dict = None):
        """Gets multiline string and generates a map based on it"""
        self.objects = objects

        if mapping is None:
            mapping = {
                "1": Wall,
                "0": Empty
            }

        if type(level) is str:
            level = level.split("\n")

        self.map = list()
        self.walls = []
        self.seeds = []

        for y, row in enumerate(level):
            if row:
                self.map.append(
                    [
                        mapping.get(tile, self.type(tile, x, y))(x * Settings.cellSizeW, y * Settings.cellSizeH)
                        for x, tile in enumerate(row)
                    ]
                )
        super().__init__(0, 0, Settings.worldWidth*Settings.cellSizeW, Settings.worldHeight*Settings.cellSizeH)

    def type(self, tile, x, y):
        if tile == 0:
            self.seeds.append(Seed(x * Settings.cellSizeW, y * Settings.cellSizeH))
            return Empty
        elif tile == 1:
            self.walls.append(pygame.Rect(x * Settings.cellSizeW, y * Settings.cellSizeH, Settings.cellSizeW, Settings.cellSizeH))
            return Wall
        else:
            return UndefinedCell

    def activate(self):
        super(Field, self).activate()
        for row in self.map:
            for cell in row:
                cell.activate()

    def logic(self):
        pass

    def draw(self, screen):
        for row in self.map:
            for tile in row:
                tile.draw(screen)
        for seed in self.seeds:
            seed.draw(screen)
