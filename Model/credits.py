import pygame
from pygame.locals import *
from background_anime import BackgroundAnime
from utils_game import load_image
from utils_game import PATH

pygame.init()
pygame.display.set_caption('End credits')
screen = pygame.display.set_mode((800, 600))
screen_r = screen.get_rect()
font = pygame.font.Font("../Fonts/gumbonormal.ttf", 30)
clock = pygame.time.Clock()
imagesBackground = [load_image(PATH + "frame_00.png"), load_image(PATH + "frame_01.png"), load_image(PATH + "frame_02.png"),
                    load_image(PATH + "frame_03.png"), load_image(PATH + "frame_04.png"), load_image(PATH + "frame_05.png"),
                    load_image(PATH + "frame_06.png"), load_image(PATH + "frame_07.png"), load_image(PATH + "frame_08.png"),
                    load_image(PATH + "frame_09.png"), load_image(PATH + "frame_10.png"), load_image(PATH + "frame_11.png"),
                    load_image(PATH + "frame_12.png"), load_image(PATH + "frame_13.png"), load_image(PATH + "frame_14.png")]
background_anime = BackgroundAnime(imagesBackground)
spriteGroup = pygame.sprite.Group(background_anime)

def drawCredits():

    credit_list = ["GameJam IUT2 2020"," ","Bubble Escape"," "," ","Julien - Graphiste"," ","Victor - Graphiste et Animateur"," ", "Theo - Developpeur"," ", "Teo - Developpeur et Sound Designer", "" , "Christopher - Game Director", "",
                   "Technologie : Python 3", "", "Librairie : PyGame", "", "Outils : PyCharm, Git, Gimp"," ",
                   "Liens pour les Ressources utilisées : ", " ", "https://ksvr.itch.io", " https://pixabay.com/fr","https://opengameart.org","https://prettybittypixels.tumblr.com",
                   "https://www.picmix.com","https://wall.alphacoders.com"]

    texts = []
    for i, line in enumerate(credit_list):
        s = font.render(line, 0, (52, 219, 235))
        r = s.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 45)
        texts.append((r, s))

    while True:
        dt = clock.tick(60) / 1000

        spriteGroup.update(dt)
        spriteGroup.draw(screen)

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                return

    #mouvement des images
        for r, s in texts:
            r.move_ip(0, -1)
            screen.blit(s, r)

        #si fin du texte alors on quitte
        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        pygame.display.flip()

        # cap framerate at 60 FPS
        clock.tick(60)

def drawExplication():
    credit_list = ["Bienvenue dans Bubble Escape ", "Vous êtes la dernière bulle", "de la terre et devez survivre",
                   "Ne faites confiance à personne","surtout aux vents", "et à ces satanés piafs !"," "," "
                   ,"Dirigez vous avec : ","Les FLÈCHES directionnelles"," et boostez vous avec ESPACE","Peut-être trouverez vous de", "l'aide dans ce monde désolé ?"]

    texts = []
    for i, line in enumerate(credit_list):
        s = font.render(line, 0, (52, 219, 235))
        r = s.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 45)
        texts.append((r, s))

    while True:
        dt = clock.tick(60) / 1000

        spriteGroup.update(dt)
        spriteGroup.draw(screen)

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        # mouvement des images
        for r, s in texts:
            r.move_ip(0, -1)
            screen.blit(s, r)

        # si fin du texte alors on quitte
        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        pygame.display.flip()

        # cap framerate at 60 FPS
        clock.tick(60)


