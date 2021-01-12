import random
import pygame

class UnitWarrior(pygame.sprite.Sprite):
    def __init__(self, x, y, image, group):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect(center=(x, y))
        self.add(group)

        self.health = 40
        self.min_damage = 0
        self.max_damage = 10
        self.is_alive = True
        self.x = x
        self.y = y
        self.dx = 50
        self.dy = 50

    def level_up(self):
        self.health += 10
        self.min_damage += 2
        self.max_damage += 3

    def check_health(self):
        if self.health <= 0:
            self.is_alive = False

    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)

    def update(self, *args):
        if args:
            if args[0] == 'turn':
                pos = args[1]
                if (self.x - (self.dx / 2) < pos[0] < self.x + (self.dx / 2)) and (
                        self.y - (self.dy / 2) < pos[1] < self.y + (self.dy / 2)):
                    pressed = pygame.mouse.get_pressed()
                    if pressed[0]:
                        print('You pressed')
        self.rect = self.image.get_rect(center=(self.x, self.y))