from classes_lib.Cell import Cell
from classes_lib.UnitWarrior import UnitWarrior
import pygame


class GameField:
    def __init__(self):
        self.cells_and_units = pygame.sprite.Group()
        for y in range(4, 7):
            line = []
            for x in range(4, 12):
                if y == 5 and x == 4:
                    unit1 = UnitWarrior(x * 50, y * 50, pygame.image.load('D:/PythonProjects/PyGames/SimpleTurnBasedGame/assets/warrior.png').convert_alpha(), self.cells_and_units)
                elif y == 5 and x == 11:
                    unit2 = UnitWarrior(x * 50, y * 50, pygame.image.load('D:/PythonProjects/PyGames/SimpleTurnBasedGame/assets/warrior.png').convert_alpha(), self.cells_and_units)
                else:
                    cell = Cell(x * 50, y * 50, pygame.image.load('D:/PythonProjects/PyGames/SimpleTurnBasedGame/assets/cell.png').convert_alpha(), self.cells_and_units)

    def update(self):
        self.cells_and_units.update()

    def draw(self, screen):
        self.cells_and_units.draw(screen)