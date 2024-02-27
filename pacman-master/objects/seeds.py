from objects.images import Image


class Seed(Image):
    def __init__(self, x, y):
        filename = "images/seed.png"
        super().__init__(filename, x, y)
        self.bonus = 1


class Cherry(Seed):
    def __init__(self, x, y):
        filename = "images/unique_seed.png"
        super().__init__(filename, x, y)
        self.bonus = 400


class Energizer(Seed):
    def __init__(self, x, y):
        filename = "images/unique_seed.png"
        super().__init__(filename, x, y)
        self.bonus = 0
