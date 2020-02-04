import pygame
import random


class Obstacle:
    def __init__(self, speed):
        self.img = pygame.Surface((50, 10))
        self.img = self.img.convert()
        self.img.fill((255, 0, 0))
        self.pos = self.img.get_rect().move(500, 300)
        self.rect = self.img.get_rect()
        self.speed = speed

    def fall(self):
        self.pos = self.pos.move(0, self.speed)

    def windTouch(self, target):
        hitbox = self.rect
        print('hitbox')
        print(hitbox)
        print('target')
        print(target)
        if(hitbox.colliderect(target)):
            return True
        else:
            return False