from player import Player
import pygame
from utils_game import load_image
from utils_game import PATH
from utils_game import scale_image


Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)



selector = 1
placement = 200
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

        self.vitesseAcceleration = 0
        self.vitesseBullePercee = 0
        self.all_sprites = pygame.sprite.Group(self.player)





