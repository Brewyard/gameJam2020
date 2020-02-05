import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('../Images/bulle_redim.png')
        self.rect = self.image.get_rect()  # permet de recuperer les coordonnees du player
        self.rect.x = 300
        self.rect.y = 300
        self.velocity = 5
        self.boost = 20
        self.pointVie = 10
        self.width = self.rect.width
        self.height = self.rect.height

    # mouvement pour les niveaux verticaux (deplacement gauche/droite)
    def move_right(self):
        self.rect.x = self.rect.x + self.velocity

    def move_left(self):
        self.rect.x = self.rect.x - self.velocity

    def souffler(self, moveX, moveY):
        # depend de la taille de la bulle
        print('moveY')
        print(moveY)
        print('height')
        print(self.rect.height/50)

        if moveX <= 0:
            self.rect.x += moveX + (self.rect.width / 90)
        else:
            self.rect.x += moveX - (self.rect.width / 90)

        if moveY <= 0:
            self.rect.y += moveY + (self.rect.height / 90)
        else:
            self.rect.y += moveY - (self.rect.height / 90)

    # mouvement pour niveaux horizontaux (deplacement haut/bas)
    def move_down(self):
        self.rect.y = self.rect.y + self.velocity

    def move_up(self):
        self.rect.y = self.rect.y - self.velocity

    # methode permettant d'ajouter le sprint en hauteur (AJOUTER la vitesse au background et non a la bulle car la camera est sur la bulle)
    def sprint_up(self):
        self.rect.y = self.rect.y + self.boost

    def sprint_side(self):
        self.rect.x = self.rect.y + self.boost

    def retrecirOuAgrandir(self, width, height):
        if (width > 50):
            self.image = pygame.transform.smoothscale(self.image, (width, height))
            # sauvegarde x et y
            sauvX = self.rect.x
            sauvY = self.rect.y
            self.rect = self.image.get_rect()
            # replace x et y
            self.rect.x = sauvX
            self.rect.y = sauvY
            self.width = self.rect.width
            self.height = self.rect.height
            return True
        else:
            # trop petite
            return False
