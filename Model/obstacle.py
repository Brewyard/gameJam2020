import pygame
import random


class Obstacle:
    def __init__(self, speed):
        longueurVent = random.randint(10, 500)
        self.img = pygame.Surface((longueurVent, 10))
        self.img = self.img.convert()
        self.img.fill((255, 0, 0))
        self.rect = self.img.get_rect().move(random.randint(0, 1) * (800 - longueurVent), 0)
        self.speed = speed

    def fall(self):
        self.rect = self.rect.move(0, self.speed)

    def windTouch2(self, target):
        hitbox = self.rect # inflate(5, 5)
        print('target')
        print(target)
        print('me')
        print(hitbox)
        if hitbox.colliderect(target):
            return True
        else:
            return False
