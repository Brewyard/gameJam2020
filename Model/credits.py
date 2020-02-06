import pygame
from pygame.locals import *

pygame.init()
pygame.display.set_caption('End credits')
screen = pygame.display.set_mode((800, 600))
screen_r = screen.get_rect()
font = pygame.font.Font("../Fonts/Polo Bubble.ttf", 45)
clock = pygame.time.Clock()

def drawCredits():

    credit_list = ["     GameJam IUT2 2020"," ","Bubble Escape"," "," ","Julien - Graphiste",
                   " ","Victor - Graphiste et Animateur"," ", "Theo - Developpeur"," ", "Teo - Developpeur et Sound Designer", "" , "Christopher - Game Director", "",
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
        for e in pygame.event.get():
            if e.type == QUIT or e.type == KEYDOWN and e.key == pygame.K_ESCAPE:
                return

        screen.fill((255, 255, 255))

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

