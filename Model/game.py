from player import Player
import pygame
Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)

import pygame

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
        self.vitesse = 0




    def jeu(self,screen,rect):
       # imageMenu = pygame.image.load("../Images/background_Menu.jpg")
       # screen.blit(imageMenu, rect)
        pass

