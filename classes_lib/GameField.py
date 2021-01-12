from classes_lib.Cell import Cell
from classes_lib.UnitWarrior import UnitWarrior
import pygame


class GameField:
    choosen_unit = None

    def __init__(self):
        self.cells_and_units = pygame.sprite.Group()
        for y in range(4, 7):
            line = []
            for x in range(4, 12):
                if y == 5 and x == 4:
                    continue
                elif y == 5 and x == 11:
                    continue
                else:
                    cell = Cell(x * 50, y * 50, pygame.image.load('D:/PythonProjects/PyGames/SimpleTurnBasedGame/assets/cell.png').convert_alpha(), self.cells_and_units)
        unit2 = UnitWarrior(4 * 50, 5 * 50, pygame.image.load(
            'D:/PythonProjects/PyGames/SimpleTurnBasedGame/assets/warrior.png').convert_alpha(), self.cells_and_units)
        unit1 = UnitWarrior(11 * 50, 5 * 50, pygame.image.load(
            'D:/PythonProjects/PyGames/SimpleTurnBasedGame/assets/warrior.png').convert_alpha(), self.cells_and_units)

    def update(self):
        self.cells_and_units.update()

    def draw(self, screen, ):
        self.cells_and_units.draw(screen)

    def make_turn_cell(self, pos):
        self.cells_and_units.update('turn', pos)

