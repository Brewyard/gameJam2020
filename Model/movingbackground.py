from obstacle import Obstacle
import pygame
import random


class MovingBackground:  # avec un sprite après
    def __init__(self):
        self.obstacles = []
        self.area = pygame.display.get_surface().get_rect()
        self.generateObstacles()
        self.windDirection = 0 # O pour souffle vers la gauche et 1 pour souffle vers la droite
        self.windForce = 0;

    def generateObstacles(self):
        if len(self.obstacles) > 20:
            self.obstacles = self.obstacles[9:]
        obstacle = Obstacle(1)
        self.obstacles.append(obstacle)

    def fall(self):
        for obstacle in self.obstacles:
            obstacle.fall()

    def addObstacles(self):
        self.generateObstacles()

    def windTouch(self, target):
        touch = False
        for obstacle in self.obstacles:
            if obstacle.windTouch2(target):
                touch = True
                if obstacle.rect.left == 0: # c'est un souffle vers la droite
                    self.windDirection = 1
                else:
                    self.windDirection = 0
                self.windForce = obstacle.rect.width / 100
        return touch
