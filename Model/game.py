from player import Player

class Game():
    def __init__(self):
        self.player = Player()
        self.pressed = {
            "touche fleche droite" : True,
            "touche fleche gauche": False,
            "touche fleche space" : False
        }

        if self.pressed.__sizeof__() > 10:
            self.pressed.clear()