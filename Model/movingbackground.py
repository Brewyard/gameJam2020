from obstacle import Obstacle
import pygame
import random


class MovingBackground:  # avec un sprite après
    def __init__(self):
        self.obstacles = []
        self.area = pygame.display.get_surface().get_rect()
        self.generateObstacles()

    def generateObstacles(self):
        if len(self.obstacles) > 10:
            self.obstacles = self.obstacles[4:]
        i = 0
        while i < random.randint(1, 2):
            obstacle = Obstacle(1)
            self.obstacles.append(obstacle)
            i += 1

    def fall(self):
        for obstacle in self.obstacles:
            obstacle.fall()

    def addObstacles(self):
        self.generateObstacles()

    def windTouch(self, target):
        print(self.obstacles)
        touch = False
        for obstacle in self.obstacles:
            touch = obstacle.windTouch2(target)
        return touch
