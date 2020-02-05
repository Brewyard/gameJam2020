from obstacle import Obstacle
import pygame
import random


class MovingBackground():  # avec un sprite après
    def __init__(self, images):
        self.images = images
        self.obstacles = []
        self.area = pygame.display.get_surface().get_rect()
        self.generateObstacles()
        self.windDirection = 0  # O pour souffle vers la gauche et 1 pour souffle vers la droite
        self.windForceX = 0
        self.windForceY = 0

    def generateObstacles(self):
        if len(self.obstacles) > 20:
            self.obstacles = self.obstacles[9:]
        obstacle = Obstacle(self.images)
        self.obstacles.append(obstacle)
        return obstacle

    def fall(self, vitesse):
        for obstacle in self.obstacles:
            obstacle.fall(vitesse)

    def addObstacles(self):
        self.generateObstacles()

    def windTouch(self, target):
        touch = False
        for obstacle in self.obstacles:
            if obstacle.windTouch2(target):
                touch = True
                posXDeLaBulle = target.x
                if obstacle.rect.left == 0: # c'est un souffle vers la droite
                    self.windDirection = 1
                else:
                    self.windDirection = 0
                    posXDeLaBulle += target.width

                self.windForceY = abs(posXDeLaBulle - obstacle.longueurVent)/80
                print('windforceY')
                print(self.windForceY)
                if target.bottom < obstacle.rect.top: #  si bulle au dessus de obstacle
                    self.windForceY = -self.windForceY

                self.windForceX = obstacle.rect.width / 80
        return touch
