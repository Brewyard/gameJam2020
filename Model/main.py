import pygame
pygame.init()
from game import Game

#Generer la fenetre de notre jeu
windowSize = (800,600)
origin = (0,0)
screen = pygame.display.set_mode(windowSize)
rect = pygame.Rect(origin,windowSize)
image = pygame.Surface(windowSize)
launch = True
imageMenu = pygame.image.load("../Images/background_Menu.jpg")

#chargement du jeu
game = Game()
while launch:
    print(game.pressed)
    #deplacement de la bulle(player) avec collision aux murs
    if game.pressed.get(pygame.K_LEFT) and game.player.rect.x + 55 > 0:
        game.player.move_left()
    if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x - 40  < 600  :
        game.player.move_right()
    if game.pressed.get(pygame.K_SPACE):
        game.player.move_up()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            launch = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True
        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

    screen.blit(imageMenu, rect)
    screen.blit(game.player.image,game.player.rect)
    #pygame.display.flip()
    pygame.display.update()








