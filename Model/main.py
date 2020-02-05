import pygame, time, random

pygame.init()
from game import Game
from movingbackground import MovingBackground
from utils_game import load_image
from utils_game import PATH
from utils_game import scale_image

# Color
transparent = (0, 0, 0, 0)
# Generer la fenetre de notre jeu
windowSize = (800, 600)
origin = (0, 0)
screen = pygame.display.set_mode(windowSize)
rect = pygame.Rect(origin, windowSize)
image = pygame.Surface(windowSize)
imageJeu = pygame.image.load("../Images/background.png")
imageJeu = pygame.transform.scale(imageJeu,(800,600))

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
imagesVent = [load_image(PATH + "vent1.png"), load_image(PATH + "vent2.png"), load_image(PATH + "vent3.png"),
              load_image(PATH + "vent4.png"), load_image(PATH + "vent5.png"), load_image(PATH + "vent6.png"),
              load_image(PATH + "vent7.png"), load_image(PATH + "vent8.png"), load_image(PATH + "vent9.png"),
              load_image(PATH + "vent10.png"), load_image(PATH + "vent11.png"), load_image(PATH + "vent12.png"),
              load_image(PATH + "vent13.png"), load_image(PATH + "vent14.png"), load_image(PATH + "vent15.png"),
              load_image(PATH + "vent16.png")]

movingBackground = MovingBackground(imagesVent)
obstacle2 = movingBackground.generateObstacles()
game.all_sprites.add(obstacle2)


# game.menu(screen)
score = 0
def gameOver():
    global score
    # pb : fait le son en double si on meurt alors sond pop et image disparait
    bubble_pop.play()
    #enregistrement du score dans un fichier
    f = open('../highscore.txt', 'r')
    highscore = int(f.read())
    f.close()
    if score >= highscore:
        f = open('../highscore.txt','w')
        f.write(str(score))
        f.close()

    game.player.image.fill(transparent)
    grey = (128, 128, 128)
    pygame.display.flip()

    time.sleep(1)
    return


# boucle principale
def playing(vitesseAcceleration):
    game.vitesseAcceleration = vitesseAcceleration
    intervalleAleatoire = random.randint(1, 100)
    compteTours = 0
    souffle = False
    secondesDeSouffle = 0
    debut_souffle = pygame.time.get_ticks()

    while launch:
        global score
        score += 1
        clock.tick(60)
        dt = clock.tick(60) / 1000
        # game.menu(screen)
        # background_music.play()
        screen.blit(imageJeu, rect)
        # creation obstacles
        # intervalle random de temps pour la generation d'obstacle
        if compteTours == intervalleAleatoire:
            obstacle1 = movingBackground.generateObstacles()
            compteTours = 0
            intervalleAleatoire = random.randint(1, 100)
            game.all_sprites.add(obstacle1)

        movingBackground.fall(game.vitesseAcceleration + game.vitesseBullePercee)
        # for obstacle in movingBackground.obstacles:
        #     screen.blit(obstacle.img, obstacle.rect)

        # si bulle touche obstacle
        if movingBackground.windTouch(game.player.rect):
            # souffler de l'air sur la bulle
            souffle = True
            debut_souffle = pygame.time.get_ticks()
            secondesDeSouffle = 0

        # deplacement de la bulle(player) avec collision aux murs
        if souffle and secondesDeSouffle < 1:  # il ne peut pas se deplacer le temps du souffle
            if movingBackground.windDirection == 0:  # souffle à gauche
                game.player.souffler(-movingBackground.windForceX, movingBackground.windForceY)
            else:
                game.player.souffler(movingBackground.windForceX, movingBackground.windForceY)
        else:
            if game.pressed.get(pygame.K_LEFT):
                game.player.move_left(5)
            elif game.pressed.get(pygame.K_RIGHT):
                game.player.move_right(5)
            else:
                game.player.velocityX = 0
            souffle = False

        if game.pressed.get(pygame.K_SPACE):
            # reduire taille bulle et accelerer bulle, la bulle etant plus petite, elle resiste moins au vent
            ilPeut = game.player.retrecirOuAgrandir(game.player.width - 3, game.player.height - 3)  # retrecit bulle
            if ilPeut:
                game.vitesseBullePercee += 1  # augmente vitesse
        else:
            game.vitesseBullePercee = 0

        if rect.contains(game.player.rect):
            riendutout = 0
        else:
            print(score)
            gameOver()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False

        game.all_sprites.update(dt)
        # screen.blit(game.player.image, game.player.rect)
        game.all_sprites.draw(screen)
        pygame.display.update()
        compteTours += 1

        if souffle:
            secondesDeSouffle = (pygame.time.get_ticks() - debut_souffle) / 1000

        if rect.contains(movingBackground.obstacles[0]):
            rien = 0
        else:
            del movingBackground.obstacles[0]
