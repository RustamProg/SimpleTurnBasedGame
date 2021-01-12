import pygame


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, image, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

        self.x = x
        self.y = y
        self.dx = 50
        self.dy = 50
        self.contains_unit = None

    def add_unit(self, unit):
        self.contains_unit = unit

    def remove_unit(self):
        self.contains_unit = None

    def is_contains_unit(self):
        if self.contains_unit is None:
            return False
        else:
            return True

    def update(self, *args):
        if args:
            if args[0] == 'destroy':
                pos = args[1]
                if (self.x - (self.dx / 2) < pos[0] < self.x + (self.dx / 2)) and (self.y - (self.dy / 2) < pos[1] < self.y + (self.dy / 2)):
                    self.kill()



