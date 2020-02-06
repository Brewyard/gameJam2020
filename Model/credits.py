import pygame
from pygame.locals import *
from background_anime import BackgroundAnime
from utils_game import load_image
from utils_game import PATH

pygame.init()
pygame.display.set_caption('End credits')
screen = pygame.display.set_mode((800, 600))
screen_r = screen.get_rect()
font = pygame.font.Font("../Fonts/gumbonormal.ttf", 40)
clock = pygame.time.Clock()
imagesBackground = [load_image(PATH + "frame_00.png"), load_image(PATH + "frame_01.png"), load_image(PATH + "frame_02.png"),
                    load_image(PATH + "frame_03.png"), load_image(PATH + "frame_04.png"), load_image(PATH + "frame_05.png"),
                    load_image(PATH + "frame_06.png"), load_image(PATH + "frame_07.png"), load_image(PATH + "frame_08.png"),
                    load_image(PATH + "frame_09.png"), load_image(PATH + "frame_10.png"), load_image(PATH + "frame_11.png"),
                    load_image(PATH + "frame_12.png"), load_image(PATH + "frame_13.png"), load_image(PATH + "frame_14.png")]
background_anime = BackgroundAnime(imagesBackground)
spriteGroup = pygame.sprite.Group(background_anime)

def drawCredits():

    credit_list = ["     GameJam IUT2 2020"," ","Bubble Escape"," "," ","Julien - Graphiste",
                   " ","Victor - Graphiste"," ", "Theo - Developpeur"," ", "Teo - Developpeur et Sound Designer", "" , "Christopher - Game Director", "",
                   "Technologie : Python 3", "", "Librairies : PyGame", "", "Outils : PyCharm, Git, Gimp"]

    texts = []
    # we render the text once, since it's easier to work with surfaces
    # also, font rendering is a performance killer
    for i, line in enumerate(credit_list):
        s = font.render(line, 0, (52, 219, 235))
        # we also create a Rect for each Surface.
        # whenever you use rects with surfaces, it may be a good idea to use sprites instead
        # we give each rect the correct starting position
        r = s.get_rect(centerx=screen_r.centerx, y=screen_r.bottom + i * 45)
        texts.append((r, s))

    while True:
        dt = clock.tick(60) / 1000

        spriteGroup.update(dt)
        spriteGroup.draw(screen)

        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                return


        # screen.fill((255, 255, 255))

        for r, s in texts:
            # now we just move each rect by one pixel each frame
            r.move_ip(0, -1)
            # and drawing is as simple as this
            screen.blit(s, r)

        # if all rects have left the screen, we exit
        if not screen_r.collidelistall([r for (r, _) in texts]):
            return

        # only call this once so the screen does not flicker
        pygame.display.flip()

        # cap framerate at 60 FPS
        clock.tick(60)

