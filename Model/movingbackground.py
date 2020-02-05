from obstacle import Obstacle
import pygame
import random


class MovingBackground():  # avec un sprite après
    def __init__(self, images):
        self.images = images
        self.obstacles = []
        self.area = pygame.display.get_surface().get_rect()
        self.generateObstacles()
        self.windDirection = 0  # O à 360 degres : 0 --> à droite
        self.windForce = 0

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
                self.windForce = obstacle.longueurVent/20
                self.windDirection = obstacle.angle
        return touch
