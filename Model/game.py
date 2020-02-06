from player import Player
import pygame
from utils_game import load_image
from utils_game import PATH
from utils_game import scale_image
from boost import BubbleBoost
from bird import Bird
import random


class Game():
    def __init__(self):
        imagesBulle = [load_image(PATH + "bubble.png"), load_image(PATH + "bubble75horizon.png"), load_image(PATH + "bubble50horizon.png"),
                  load_image(PATH + "bubble75horizon.png"), load_image(PATH + "bubble.png"), load_image(PATH + "bubble75verti.png"),
                  load_image(PATH + "bubble50verti.png"), load_image(PATH + "bubble75verti.png")]
        imagesBulleScaled = []
        for image in imagesBulle:
            imagesBulleScaled.append(scale_image(image, 100, 100))

        self.player = Player(imagesBulleScaled)
        self.pressed = {
            "touche fleche droite" : True,
            "touche fleche gauche": False,
            "touche fleche space" : False
        }
        self.boosts = []

        self.imagesBoost = [load_image(PATH + "bubbles_group_1.png"), load_image(PATH + "bubbles_group_2.png"), load_image(PATH + "bubbles_group_3.png"),
                       load_image(PATH + "bubbles_group_4.png"), load_image(PATH + "bubbles_group_5.png")]

        self.vitesseAcceleration = 0
        self.vitesseBullePercee = 0
        self.all_sprites = pygame.sprite.Group(self.player)

        self.imagesBird = []

        self.imagesBird.append([scale_image(load_image(PATH + "bird_blue_1.png"), 50, 50), scale_image(load_image(PATH + "bird_blue_2.png"), 50, 50),
                                scale_image(load_image(PATH + "bird_blue_3.png"), 50, 50)])
        self.imagesBird.append([scale_image(load_image(PATH + "bird_brown_1.png"), 50, 50), scale_image(load_image(PATH + "bird_brown_2.png"), 50, 50),
                                scale_image(load_image(PATH + "bird_brown_3.png"), 50, 50)])
        self.imagesBird.append([scale_image(load_image(PATH + "bird_robin_1.png"), 50, 50), scale_image(load_image(PATH + "bird_robin_2.png"), 50, 50),
                                scale_image(load_image(PATH + "bird_robin_3.png"), 50, 50)])
        self.birds = []


    def resetGame(self):
        self.imagesBird.clear()
        self.vitesseAcceleration = 0
        self.vitesseBullePercee = 0
        self.birds.clear()


    def addBoost(self):
        boost = BubbleBoost(self.imagesBoost)
        self.boosts.append(boost)
        return boost

    def addBird(self):
        birdIndice = random.randint(0, 2)
        bird = Bird(self.imagesBird[birdIndice])
        self.birds.append(bird)
        return bird



