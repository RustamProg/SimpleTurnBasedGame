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

    def level_up(self):
        self.health += 10
        self.min_damage += 2
        self.max_damage += 3

    def check_health(self):
        if self.health <= 0:
            self.is_alive = False

    def get_damage(self):
        return random.randint(self.min_damage, self.max_damage)

    def update(self):
        self.x -= 1
        self.y -= 1
        self.rect = self.image.get_rect(center=(self.x, self.y))

