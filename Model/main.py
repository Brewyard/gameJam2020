import pygame, time, random

pygame.init()
import math
from game import Game
from movingbackground import MovingBackground
from obstacle import Obstacle

selectorGameOver = 1
placement = 300
from utils_game import load_image
from utils_game import PATH
from utils_game import scale_image

# Color
transparent = (0, 0, 0, 0)
# Generer la fenetre de notre jeu
windowSize = (800, 600)
origin = (0, 0)
pygame.display.set_caption('Joue TARBANAK')
screen = pygame.display.set_mode(windowSize)
rect = pygame.Rect(origin, windowSize)
image = pygame.Surface(windowSize)
imageJeu = pygame.image.load("../Images/background.png")
imageJeu = pygame.transform.scale(imageJeu, (800, 600))

launch = True
menu = True
jeu = False
# generation de sons
bubble_pop = pygame.mixer.Sound('../Sounds/bubble-pop.wav')
windy_today = pygame.mixer.Sound('../Sounds/wind.wav')
background_music = pygame.mixer.Sound('../Sounds/Play.wav')

# chargement du jeu
game = Game()
clock = pygame.time.Clock()

# generation background
# try:
imagesVent = [load_image(PATH + "vent1.png"), load_image(PATH + "vent2.png"), load_image(PATH + "vent3.png"),
              load_image(PATH + "vent4.png"), load_image(PATH + "vent5.png"), load_image(PATH + "vent6.png"),
              load_image(PATH + "vent7.png"), load_image(PATH + "vent8.png"), load_image(PATH + "vent9.png"),
              load_image(PATH + "vent10.png"), load_image(PATH + "vent11.png"), load_image(PATH + "vent12.png"),
              load_image(PATH + "vent13.png"), load_image(PATH + "vent14.png"), load_image(PATH + "vent15.png"),
              load_image(PATH + "vent16.png")]
# except:
#     print('nani')
# imagesVent = [load_image(PATH + "wind-sens-1.png"), load_image(PATH + "wind-sens-2.png"), load_image(PATH + "wind-sens-1.png")]

movingBackground = MovingBackground(imagesVent)
obstacle2 = movingBackground.generateObstacles()
game.all_sprites.add(obstacle2)

# game.menu(screen)
score = 0


def gameOver():
    Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
    Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)
    global score, placement, selectorGameOver
    global windowSize, origin, screen
    placement = 300
    selectorGameOver = 1
    # pb : fait le son en double si on meurt alors son pop et image disparait
    bubble_pop.play()
    game.player.image.fill(transparent)
    # enregistrement du score dans un fichier
    f = open('../highscore.txt', 'r')
    highscore = int(f.read())
    f.close()
    if score >= highscore:
        f = open('../highscore.txt', 'w')
        f.write(str(score))
        f.close()

    f = open('../highscore.txt', 'r')
    highscore = int(f.read())
    f.close()
    windowSize = (800, 600)
    origin = (0, 0)

    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin, windowSize)
    image = pygame.Surface(windowSize)
    imageJeu = pygame.image.load("../Images/background_Menu.jpg")
    pygame.display.set_caption('GameOver TARBANAK')

    textMort = Texty.render('Game Over ', 0, (0, 0, 255))
    textRetour = Texty.render('Retour ', 0, (0, 0, 255))
    textHighscore = Texty.render("Highscore : " + str(highscore), 0, (255, 0, 0))
    textScore = Texty.render("Score : " + str(score), 0, (255, 0, 0))

    imageFleche = pygame.image.load("../Images/fleche_rouge.jpg")
    imageFleche = pygame.transform.scale(imageFleche, (30, 30))
    screen.blit(textRetour, (300, 300))
    screen.blit(textMort, (300, 200))
    screen.blit(textHighscore, (50, 50))
    screen.blit(textScore, (50, 100))

    if selectorGameOver == 1:
        placement == 300
    screen.blit(imageFleche, (260, placement))
    pygame.display.update()


# boucle principale
def playing(vitesseAcceleration):
    game.vitesseAcceleration = vitesseAcceleration
    intervalleAleatoire1 = random.randint(1, 100)
    compteTours1 = 0
    intervalleAleatoire2 = random.randint(1, 1000)
    compteTours2 = 0
    intervalleAleatoire3 = random.randint(1, 1000)
    compteTours3 = 0
    souffle = False
    secondesDeSouffle = 0
    debut_souffle = pygame.time.get_ticks()
    background_music.play()

    en_jeu = False
    while launch:
        en_jeu = True
        global score
        clock.tick(60)
        dt = clock.tick(60) / 1000
        # game.menu(screen)
        # background_music.play()
        screen.blit(imageJeu, rect)
        # creation obstacles
        # intervalle random de temps pour la generation d'obstacle
        if compteTours1 == intervalleAleatoire1:
            obstacle1 = movingBackground.generateObstacles()
            compteTours1 = 0
            intervalleAleatoire1 = random.randint(1, 100)
            game.all_sprites.add(obstacle1)

        # intervalle random de temps pour la generation de boost
        if compteTours2 == intervalleAleatoire2:
            boost = game.addBoost()
            compteTours2 = 0
            intervalleAleatoire2 = random.randint(1, 1000)
            game.all_sprites.add(boost)

        # intervalle random de temps pour la generation de bird
        if compteTours3 == intervalleAleatoire3:
            bird = game.addBird()
            compteTours3 = 0
            intervalleAleatoire3 = random.randint(1, 1000)
            game.all_sprites.add(bird)

        movingBackground.fall(game.vitesseAcceleration + game.vitesseBullePercee)
        # for obstacle in movingBackground.obstacles:
        #     screen.blit(obstacle.img, obstacle.rect)

        # si bulle touche obstacle
        if movingBackground.windTouch(game.player.rect):
            windy_today.play()
            # souffler de l'air sur la bulle
            souffle = True
            debut_souffle = pygame.time.get_ticks()
            secondesDeSouffle = 0

        # si bulle touche boost
        for boost in game.boosts:
            if boost.touch(game.player.rect):
                print('ca touche mamene')
                #  gonfler la bulle et delete le boost
                game.player.retrecirOuAgrandir(game.player.width + 15, game.player.height + 15)
                game.boosts.remove(boost)
                # game.all_sprites.remove(boost)
            # si boost sorti de l'ecran
            if not rect.inflate(200, 200).contains(boost.rect):
                game.boosts.remove(boost)
                # game.all_sprites.remove(boost)

        # si bulle touche boost
        for bird in game.birds:
            if bird.touch(game.player.rect):
                # gameover
                background_music.stop()
                en_jeu = False
                return en_jeu
            # si bird sorti de l'ecran
            if not rect.inflate(200, 200).contains(bird.rect):
                game.boosts.remove(bird)
                game.all_sprites.remove(bird)

        # deplacement de la bulle(player) avec collision aux murs
        if souffle and secondesDeSouffle < 1:  # il ne peut pas se deplacer le temps du souffle
            coordonnees = math.radians(movingBackground.windDirection)
            sin = math.sin(coordonnees)
            cos = math.cos(coordonnees)
            # pour le x
            if cos * movingBackground.windForce < 0:
                force = cos * movingBackground.windForce + (game.player.width / 50)
                if force * (cos * movingBackground.windForce) < 0:  # depasser le 0
                    game.player.move_x(-1)
                else:
                    game.player.move_x(force)
            else:
                force = cos * movingBackground.windForce - (game.player.width / 50)
                if force * (cos * movingBackground.windForce) < 0:  # depasser le 0
                    game.player.move_x(1)
                else:
                    game.player.move_x(force)
            # pour le y
            if (-sin) * movingBackground.windForce < 0:
                force = (-sin) * movingBackground.windForce + (game.player.width / 10)
                if force * ((-sin) * movingBackground.windForce) < 0:  # depasser le 0
                    game.player.move_y(-1)
                else:
                    game.player.move_y(force)
            else:
                force = (-sin) * movingBackground.windForce - (game.player.width / 10)
                if force * ((-sin) * movingBackground.windForce) < 0:  # depasser le 0
                    game.player.move_y(1)
                else:
                    game.player.move_y(force)
        else:
            if game.pressed.get(pygame.K_LEFT):
                game.player.move_x(-10)
            elif game.pressed.get(pygame.K_RIGHT):
                game.player.move_x(10)
            elif game.pressed.get(pygame.K_DOWN):
                game.player.move_y(10)
            elif game.pressed.get(pygame.K_UP):
                game.player.move_y(-10)
            souffle = False

        if game.pressed.get(pygame.K_SPACE):
            # reduire taille bulle et accelerer bulle, la bulle etant plus petite, elle resiste moins au vent
            ilPeut = game.player.retrecirOuAgrandir(game.player.width - 2, game.player.height - 2)  # retrecit bulle
            if ilPeut:
                game.player.move_y(-10)
        # else:
        #     game.vitesseBullePercee = 0

        if rect.inflate(150, 150).contains(game.player.rect):
            score += 1
            riendutout = 0
        else:
            background_music.stop()
            en_jeu = False
            return en_jeu

            # drawMenu()

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
        compteTours1 += 1
        compteTours2 += 1
        compteTours3 += 1

        if souffle:
            secondesDeSouffle = (pygame.time.get_ticks() - debut_souffle) / 1000

        if movingBackground.obstacles:
            if rect.contains(movingBackground.obstacles[0]):
                rien = 0
            else:
                del movingBackground.obstacles[0]

        game.player.velocityX = 0
        game.player.velocityY = 0
