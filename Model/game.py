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

        imagesBulleBoosted = [load_image(PATH + "bubble_boosted_1.png"), load_image(PATH + "bubble_boosted_2.png"),
                       load_image(PATH + "bubble_boosted_3.png"),
                       load_image(PATH + "bubble_boosted_4.png")]
        imagesBulleBoostedScaled = []
        for image in imagesBulleBoosted:
            imagesBulleBoostedScaled.append(scale_image(image, 100, 100))

        self.player = Player(imagesBulleScaled, imagesBulleBoostedScaled)
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

        self.frequenceBirds = 1000  # plus c'est eleve moins c'est frequent
        self.frequenceVent = 100
        self.frequenceBoost = 1000

    def resetGame(self):
        self.imagesBird.clear()
        self.vitesseAcceleration = 0
        self.vitesseBullePercee = 0
        self.birds.clear()


    def addBoost(self, vitesse):
        boost = BubbleBoost(self.imagesBoost)
        boost.speed += vitesse
        self.boosts.append(boost)
        return boost

    def addBird(self, vitesse):
        birdIndice = random.randint(0, 2)
        bird = Bird(self.imagesBird[birdIndice])
        bird.speed += vitesse
        self.birds.append(bird)
        return bird

    def setDifficulte(self, difficulte):
        self.vitesseAcceleration = difficulte
        if difficulte == 1:
            self.frequenceBirds = 500
            self.frequenceVent = 60
            self.frequenceBoost = 1200
        elif difficulte == 2:
            self.frequenceBirds = 300
            self.frequenceBoost = 1400
            self.frequenceVent = 40
        elif difficulte == 4:
            self.frequenceBirds = 100
            self.frequenceBoost = 2000
            self.frequenceVent = 25

