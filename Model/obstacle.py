import pygame
import random


class Obstacle:
    def __init__(self, speed):
        self.img = pygame.Surface((50, 10))
        self.img = self.img.convert()
        self.img.fill((0, 0, 0))
        self.pos = self.img.get_rect().move(random.randint(0, 1)*450, 0)
        self.speed = speed

    def fall(self):
        self.pos = self.pos.move(0, self.speed)

    def windTouch(self, target):
        hitbox = self.img.get_rect().inflate(-5, -5)
        return hitbox.colliderect(target)