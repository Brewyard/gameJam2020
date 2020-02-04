import pygame,time,random
pygame.init()
from game import Game
from movingbackground import MovingBackground
from obstacle import Obstacle


#Color
transparent = (0, 0, 0, 0)
#Generer la fenetre de notre jeu
windowSize = (800, 600)
origin = (0, 0)
screen = pygame.display.set_mode(windowSize)
rect = pygame.Rect(origin,windowSize)
image = pygame.Surface(windowSize)
imageJeu = pygame.image.load("../Images/background_Menu.jpg")





launch = True
menu = True
jeu = False
#generation de sons
bubble_pop = pygame.mixer.Sound('../Sounds/bubble-pop.wav')
windy_today = pygame.mixer.Sound('../Sounds/wind.wav')
background_music = pygame.mixer.Sound('../Sounds/yes.wav')
#chargement du jeu
game = Game()

#generation background
movingBackground = MovingBackground()
movingBackground.generateObstacles()

#game.menu(screen)

def gameOver():
    # pb : fait le son en double si on meurt alors sond pop et image disparait
    bubble_pop.play()
    game.player.image.fill(transparent)
    grey = (128,128,128)
    gameOverFont = pygame.font.Font('freesansbold.ttf', 72)
    gameOverSurface = gameOverFont.render('Game Over', True, grey)
    gameOverRect = gameOverSurface.get_rect()
    gameOverRect.midtop = (400, 200)
    screen.blit(gameOverSurface, gameOverRect)
    pygame.display.flip()
    time.sleep(1)



#boucle principale
def playing():
    while launch:

        #game.menu(screen)
        #background_music.play()
        screen.blit(imageJeu, rect)
        obstacle = Obstacle(1)
        screen.blit(obstacle.img, (500, 400))
        if game.player.rect.x == obstacle.rect.x and game.player.rect.y == obstacle.rect.y:
            print("CA MARCHE")
        #creation obstacles
        # intervalle random de temps pour la generation d'obstacle
        intervalle = random.randint(1, 100)
        if intervalle > 99:
            movingBackground.generateObstacles()
        for obstacle in movingBackground.obstacles:
            obstacle.fall()
            screen.blit(obstacle.img, obstacle.pos)
        print(obstacle.windTouch(game.player.rect))

        # deplacement de la bulle(player) avec collision aux murs
        if game.pressed.get(pygame.K_LEFT) and game.player.rect.x + 55 > 0:
            if game.player.rect.x - 40 <= 0: #methode contient dans la windows ??
                gameOver()
            game.player.move_left()
        if game.pressed.get(pygame.K_RIGHT) and game.player.rect.x - 40 < 600:
            if game.player.rect.x - 40 >= 590:
                gameOver()
            game.player.move_right()


        for event in pygame.event.get():
            if event.type == pygame.QUIT :
                pygame.quit()
                exit()
            elif event.key == pygame.K_ESCAPE:
                return
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False


        screen.blit(game.player.image,game.player.rect)
        pygame.display.update()








