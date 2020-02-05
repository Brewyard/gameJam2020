from player import Player



import pygame
#from levels import *

Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)



selector = 1
placement = 200
class Game():
    def __init__(self):
        self.player = Player()
        self.pressed = {
            "touche fleche droite" : True,
            "touche fleche gauche": False,
            "touche fleche space" : False
        }
        self.vitesseAcceleration = 0







