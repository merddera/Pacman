from settings import *
from objects.images import Image


class Cell(Image):
    def __init__(self, filename, x, y):
        super().__init__(filename, x, y)

        self.rect.width = Settings.cellSizeW
        self.rect.height = Settings.cellSizeH
        self.image = pygame.transform.scale(self.image, (self.rect.width, self.rect.height))


class Wall(Cell):
    def __init__(self, x, y):
        filename = "images/tile2.png"
        super().__init__(filename, x, y)


class Teleport(Cell):
    def __init__(self, x, y, other_cell):
        filename = "images/portal1.png"
        super().__init__(filename, x, y)
        self.link = other_cell


class Empty(Cell):
    def __init__(self, x, y):
        filename = "images/missing_tile.png"
        super().__init__(filename, x, y)
        self.content = []

    def trash(self):
        pass

    def rebase(self):
        pass


class UndefinedCell(Cell):
    def __init__(self, x, y):
        filename = "images/tile3.png"
        super().__init__(filename, x, y)
