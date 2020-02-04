from obstacle import Obstacle
import pygame
import random


class MovingBackground:  # avec un sprite après
    def __init__(self):
        self.obstacles = []
        self.area = pygame.display.get_surface().get_rect()
        self.generateObstacles()

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
        return touch
