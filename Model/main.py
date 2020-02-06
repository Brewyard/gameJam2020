import pygame, time, random

pygame.init()
import math
from game import Game
from movingbackground import MovingBackground
from bird import Bird
from obstacle import Obstacle
from player import Player
import pygame
import random
import sys
import os

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

MENU_SCREEN = 0
GAME_SCREEN = 1
HIGH_SCORE_SCREEN = 2
SAVE_SCORE_SCREEN = 3

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
pygame.display.set_caption('Bubble Escape')
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
# imagesVent = [load_image(PATH + "wind1.png"), load_image(PATH + "wind2.png"), load_image(PATH + "wind3.png"), load_image(PATH + "wind4.png")]

# game.menu(screen)
score = 0


def text1(word, x, y, sizeFont, r, v, b):
    # Generer la fenetre de notre jeu
    # screen = pygame.display.set_mode(windowSize)
    font = pygame.font.Font('../Fonts/gumbonormal.ttf', sizeFont)
    text = font.render("{}".format(word), True, (r, v, b))
    return screen.blit(text, (x, y))


def inpt():
    screen.fill((0, 0, 0))
    word = ""
    text1("Please enter your name: ", 100, 200, 40, 0, 153, 255)  # example asking name
    pygame.display.flip()
    done = True
    while done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    word += str(chr(event.key))
                if event.key == pygame.K_b:
                    word += chr(event.key)
                if event.key == pygame.K_c:
                    word += chr(event.key)
                if event.key == pygame.K_d:
                    word += chr(event.key)
                if event.key == pygame.K_e:
                    word += chr(event.key)
                if event.key == pygame.K_f:
                    word += chr(event.key)
                if event.key == pygame.K_g:
                    word += chr(event.key)
                if event.key == pygame.K_h:
                    word += chr(event.key)
                if event.key == pygame.K_i:
                    word += chr(event.key)
                if event.key == pygame.K_j:
                    word += chr(event.key)
                if event.key == pygame.K_k:
                    word += chr(event.key)
                if event.key == pygame.K_l:
                    word += chr(event.key)
                if event.key == pygame.K_m:
                    word += chr(event.key)
                if event.key == pygame.K_n:
                    word += chr(event.key)
                if event.key == pygame.K_o:
                    word += chr(event.key)
                if event.key == pygame.K_p:
                    word += chr(event.key)
                if event.key == pygame.K_q:
                    word += chr(event.key)
                if event.key == pygame.K_r:
                    word += chr(event.key)
                if event.key == pygame.K_s:
                    word += chr(event.key)
                if event.key == pygame.K_t:
                    word += chr(event.key)
                if event.key == pygame.K_u:
                    word += chr(event.key)
                if event.key == pygame.K_v:
                    word += chr(event.key)
                if event.key == pygame.K_w:
                    word += chr(event.key)
                if event.key == pygame.K_x:
                    word += chr(event.key)
                if event.key == pygame.K_y:
                    word += chr(event.key)
                if event.key == pygame.K_z:
                    word += chr(event.key)
                if event.key == pygame.K_RETURN:
                    done = False
                text1("Please enter your name: ", 100, 200, 40, 0, 153, 255)
                text1(word, 300, 400, 20, 0, 153, 255)
                pygame.display.flip()
    return word


def gameOver():
    font = pygame.font.Font('../Fonts/gumbonormal.ttf', 20)
    bigFont = pygame.font.Font('../Fonts/gumbonormal.ttf', 60)

    global score, placement, selectorGameOver
    global windowSize, origin, screen
    placement = 300
    selectorGameOver = 1
    bubble_pop.play()
    # game.player.image.fill(transparent)

    f = open('../highscore.txt', 'r')
    highscore = int(f.read())
    f.close()
    if score >= highscore:
        # demande le nom
        nameEntre = inpt()
        f = open('../name.txt', 'w')
        f.write(nameEntre)
        f.close()

        highscore = score
        f = open('../highscore.txt', 'w')
        f.write(str(highscore))
        f.close()

    windowSize = (800, 600)
    origin = (0, 0)

    screen = pygame.display.set_mode(windowSize)
    pygame.display.set_caption('Bubble Escape')
    textMort = bigFont.render('Game Over ', 0, (255, 0, 0))
    textHighscore = font.render("Highscore : " + str(highscore), 0, (255, 0, 0))
    textScore = font.render("Score : " + str(score), 0, (255, 0, 0))
    screen.blit(textMort, (180, 270))
    screen.blit(textHighscore, (50, 50))
    screen.blit(textScore, (50, 100))
    pygame.display.update()
    score = 0
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                return


# boucle principale
def playing(difficulte):
    game = Game()
    movingBackground = MovingBackground(imagesVent)
    obstacle2 = movingBackground.generateObstacles()
    game.all_sprites.add(obstacle2)

    game.setDifficulte(difficulte)
    intervalleAleatoireVent = random.randint(1, game.frequenceVent)
    compteToursVent = 0
    intervalleAleatoireBoost = random.randint(1, game.frequenceBoost)
    compteToursBoost = 0
    intervalleAleatoireBird = random.randint(1, game.frequenceBirds)
    compteToursBird = 0
    souffle = False
    secondesDeSouffle = 0
    debut_souffle = pygame.time.get_ticks()
    background_music.play(-1)

    compteToursGlobalPourAcceleration = 0
    vitesseBoostEtOiseauEnPlus = 0

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
        if compteToursVent == intervalleAleatoireVent:
            obstacle1 = movingBackground.generateObstacles()
            obstacle1.speed += vitesseBoostEtOiseauEnPlus
            compteToursVent = 0
            intervalleAleatoireVent = random.randint(1, game.frequenceVent)
            game.all_sprites.add(obstacle1)

        # intervalle random de temps pour la generation de boost
        if compteToursBoost == intervalleAleatoireBoost:
            boost = game.addBoost(vitesseBoostEtOiseauEnPlus)
            compteToursBoost = 0
            intervalleAleatoireBoost = random.randint(1, game.frequenceBoost)
            game.all_sprites.add(boost)

        # intervalle random de temps pour la generation de bird
        if compteToursBird == intervalleAleatoireBird:
            bird = game.addBird(vitesseBoostEtOiseauEnPlus)
            compteToursBird = 0
            intervalleAleatoireBird = random.randint(1, game.frequenceBirds)
            game.all_sprites.add(bird)

        movingBackground.fall(game.vitesseAcceleration + game.vitesseBullePercee)

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
                #  gonfler la bulle et delete le boost
                game.player.retrecirOuAgrandir(game.player.width + 15, game.player.height + 15)
                game.boosts.remove(boost)
                game.all_sprites.remove(boost)
            # si boost sorti de l'ecran
            if not rect.inflate(200, 200).contains(boost.rect):
                game.boosts.remove(boost)
                game.all_sprites.remove(boost)

        # si bulle touche boost
        for bird in game.birds:
            if bird.touch(game.player.rect):
                # gameover
                background_music.stop()
                en_jeu = False
                # game.player.resetPlayer()
                # game.resetGame()
                return en_jeu
            # si bird sorti de l'ecran
            if not rect.inflate(200, 200).contains(bird.rect):
                game.birds.remove(bird)
                game.all_sprites.remove(bird)

        # deplacement de la bulle(player) avec collision aux murs
        if souffle and secondesDeSouffle < 0.2:  # il ne peut pas se deplacer le temps du souffle
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

        if rect.inflate(150, 150).contains(game.player.rect):
            score += 1
            riendutout = 0
        else:
            background_music.stop()
            # game.player.resetPlayer()
            # game.resetGame()
            en_jeu = False
            return en_jeu

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
        pygame.display.flip()
        compteToursVent += 1
        compteToursBoost += 1
        compteToursBird += 1

        if souffle:
            secondesDeSouffle = (pygame.time.get_ticks() - debut_souffle) / 1000

        if movingBackground.obstacles:
            if rect.contains(movingBackground.obstacles[0]):
                rien = 0
            else:
                del movingBackground.obstacles[0]

        game.player.velocityX = 0
        game.player.velocityY = 0

        compteToursGlobalPourAcceleration += 1
        if compteToursGlobalPourAcceleration == 8000:
            compteToursGlobalPourAcceleration = 0
            vitesseBoostEtOiseauEnPlus += 1

        # si appuie sur entree ==> pause
        if game.pressed.get(pygame.K_RETURN):
            text1('PAUSE', 200, 200, 90, 120, 120, 120)
            pygame.display.flip()
            reprendre = False
            while not reprendre:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        reprendre = True
                        game.pressed[pygame.K_RETURN] = False
