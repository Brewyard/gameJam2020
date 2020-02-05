import pygame
from utils_game import scale_image

class Player(pygame.sprite.Sprite):
    def __init__(self, images):
        super(Player, self).__init__()
        size = (100, 100)

        self.rect = pygame.Rect((300, 300), size)
        self.images = images
        self.index = 0
        self.image = images[self.index]
        self.velocityX = 0
        self.velocityY = 0

        self.animation_time = 0.02
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

        self.boost = 20
        self.width = self.rect.width
        self.height = self.rect.height

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(self.velocityX, self.velocityY)

    def update_frame_dependent(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(self.velocityX, self.velocityY)

    def update(self, dt):
        # Switch between the two update methods by commenting/uncommenting.
        self.update_time_dependent(dt)
        # self.update_frame_dependent()

    # mouvement pour les niveaux verticaux (deplacement gauche/droite)
    def move_right(self, velocity):
        self.velocityX = velocity

    def move_left(self, velocity):
        self.velocityX = -velocity

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
        self.rect.y = self.rect.y + self.velocityX

    def move_up(self):
        self.rect.y = self.rect.y - self.velocityY

    # methode permettant d'ajouter le sprint en hauteur (AJOUTER la vitesse au background et non a la bulle car la camera est sur la bulle)
    def sprint_up(self):
        self.rect.y = self.rect.y + self.boost

    def sprint_side(self):
        self.rect.x = self.rect.y + self.boost

    def retrecirOuAgrandir(self, width, height):
        if (width > 50):
            imagesScaled = []
            for image in self.images:
                imagesScaled.append(scale_image(image, width, height))
            self.images = imagesScaled
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
