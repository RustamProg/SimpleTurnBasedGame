import pygame
from classes_lib.GameField import GameField

WIDTH = 700
HEIGHT = 480
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
field = GameField()
# Цикл игры
game_is_running = True
while game_is_running:
    # Держим цикл на правильной скорости
    clock.tick(FPS)
    # Ввод процесса (события)
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            game_is_running = False

    screen.fill(WHITE)

    field.draw(screen)

    pygame.display.update()
    pygame.time.delay(20)

    field.update()

pygame.quit()