import pygame, time, random

pygame.init()
from game import Game
from movingbackground import MovingBackground
from obstacle import Obstacle

# Color
transparent = (0, 0, 0, 0)
# Generer la fenetre de notre jeu
windowSize = (800, 600)
origin = (0, 0)
screen = pygame.display.set_mode(windowSize)
rect = pygame.Rect(origin, windowSize)
image = pygame.Surface(windowSize)
imageJeu = pygame.image.load("../Images/background_Menu.jpg")

launch = True
menu = True
jeu = False
# generation de sons
bubble_pop = pygame.mixer.Sound('../Sounds/bubble-pop.wav')
windy_today = pygame.mixer.Sound('../Sounds/wind.wav')
background_music = pygame.mixer.Sound('../Sounds/yes.wav')
# chargement du jeu
game = Game()
clock = pygame.time.Clock()

# generation background
movingBackground = MovingBackground()
movingBackground.generateObstacles()


# game.menu(screen)

def gameOver():
    # pb : fait le son en double si on meurt alors sond pop et image disparait
    bubble_pop.play()
    game.player.image.fill(transparent)
    grey = (128, 128, 128)
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurface = gameOverFont.render('Game Over', True, grey)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (400, 200)
    screen.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    time.sleep(1)



# boucle principale
def playing():
    intervalleAleatoire = random.randint(1, 100)
    compteTours = 0
    while launch:
        clock.tick(60)
        # game.menu(screen)
        # background_music.play()
        screen.blit(imageJeu, rect)
        # creation obstacles
        # intervalle random de temps pour la generation d'obstacle
        if compteTours == intervalleAleatoire:
            movingBackground.generateObstacles()
            compteTours = 0
            intervalleAleatoire = random.randint(1, 1000)

        for obstacle in movingBackground.obstacles:
            obstacle.fall()
            screen.blit(obstacle.img, obstacle.rect)

        # si bulle touche obstacle
        if movingBackground.windTouch(game.player.rect):
            return

        # deplacement de la bulle(player) avec collision aux murs
        if game.pressed.get(pygame.K_LEFT):
            game.player.move_left()
        if game.pressed.get(pygame.K_RIGHT):
            game.player.move_right()
        if rect.contains(game.player.rect):
            riendutout = 0
        else:
            gameOver()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        screen.blit(game.player.image, game.player.rect)
        pygame.display.update()
        compteTours += 1