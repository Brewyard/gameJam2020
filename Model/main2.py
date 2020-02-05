import pygame
from credits import drawCredits
from main import playing
pygame.init()
Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)
selector = 1
placement = 200
def drawMenu():
    #Generer la fenetre de notre jeu
    windowSize = (800, 600)
    origin = (0,0)
    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin,windowSize)
    image = pygame.Surface(windowSize)
    imageJeu = pygame.image.load("../Images/background_Menu.jpg")
    textTitre = Texty.render('XXX ', 0, (255, 0, 0))
    textStart = Texty.render('start', 0, (255, 0, 0))
    textCredits = Texty.render('Credits', 0, (255, 0, 0))
    textQuit = Texty.render('quit ', 0, (255, 0, 0))
    imageFleche = pygame.image.load("../Images/fleche_rouge.jpg")
    imageFleche = pygame.transform.scale(imageFleche,(30,30))
    screen.blit(textTitre, (400, 150))
    screen.blit(textStart, (400, 200))
    screen.blit(textCredits, (400, 250))
    screen.blit(textQuit, (400, 300))
    if selector == 1:
        placement = 200
    elif selector == 2:
        placement = 250
    elif selector == 3:
        placement = 300
    screen.blit(imageFleche,(200, placement))
    pygame.display.update()


run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if selector != 1:
                    selector -= 1
            elif event.key == pygame.K_DOWN:
                if selector != 3:
                    selector += 1
            elif event.key == pygame.K_RETURN and selector == 1:
                playing()
                print("je joue")
            elif event.key == pygame.K_RETURN and selector == 2:
                drawCredits()
            elif event.key == pygame.K_RETURN and selector == 3:
                pygame.quit()
                exit()

    drawMenu()



