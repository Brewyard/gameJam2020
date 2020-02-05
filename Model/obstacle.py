import pygame
import random


class Obstacle:
    def __init__(self):
        longueurVent = random.randint(10, 400)
        self.img = pygame.Surface((longueurVent, 10))
        self.img = self.img.convert()
        self.img.fill((255, 0, 0))
        self.rect = self.img.get_rect().move(random.randint(0, 1) * (800 - longueurVent), 0)
        self.speed = 1

    def fall(self, vitesse):

        self.rect.y += self.speed + vitesse

    def windTouch2(self, target):
        hitbox = self.rect.inflate(-5, -5)
        if hitbox.colliderect(target):
            return True
        else:
            return False
