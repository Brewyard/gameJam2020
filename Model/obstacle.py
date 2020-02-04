import pygame
import random


class Obstacle:
    def __init__(self, speed):
        self.img = pygame.Surface((50, 10))
        self.img = self.img.convert()
        self.img.fill((255, 0, 0))
        self.pos = self.img.get_rect().move(500, 0)
        self.speed = speed

    def fall(self):
        self.pos = self.pos.move(0, self.speed)

    def windTouch(self, target):
        hitbox = self.pos
        if hitbox.colliderect(target):
            return True
        else:
            return False
