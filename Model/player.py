import  pygame
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../Images/perso (1).png')
        self.rect = self.image.get_rect() #permet de recuperer les coordonnees du player
        self.rect.x = 300
        self.rect.y = 300
        self.velocity = 5
        self.boost = 20
        self.pointVie = 10


    #mouvement pour les niveaux verticaux (deplacement gauche/droite)
    def move_right(self):
       self.rect.x = self.rect.x + self.velocity
    def move_left(self):
        self.rect.x = self.rect.x - self.velocity

    #mouvement pour niveaux horizontaux (deplacement haut/bas)
    def move_down(self):
        self.rect.y = self.rect.y + self.velocity

    def move_up(self):
        self.rect.y = self.rect.y - self.velocity


    #methode permettant d'ajouter le sprint en hauteur (AJOUTER la vitesse au background et non a la bulle car la camera est sur la bulle)
    def sprint_up(self):
        self.rect.y = self.rect.y + self.boost

    def sprint_side(self):
        self.rect.x = self.rect.y + self.boost

