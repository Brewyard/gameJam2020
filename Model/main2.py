import pygame
from credits import drawCredits
from main import playing
from game import Game

pygame.init()
Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)
selector = 1
placement = 200
game = Game()

f = open('../highscore.txt', 'r')
highscore = int(f.read())
f.close()

def drawMenu():
    #Generer la fenetre de notre jeu
    windowSize = (800, 600)
    origin = (0,0)
    global highscore
    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin,windowSize)
    image = pygame.Surface(windowSize)
    imageJeu = pygame.image.load("../Images/background_Menu.jpg")
    textTitre = Texty.render('XXX ', 0, (255, 0, 0))
    textStart = Texty.render('start', 0, (255, 0, 0))
    textCredits = Texty.render('Credits', 0, (255, 0, 0))
    textQuit = Texty.render('quit ', 0, (255, 0, 0))
    textHighscore = Texty.render("Highscore : "+str(highscore),0,(255,0,0))
    imageFleche = pygame.image.load("../Images/fleche_rouge.jpg")
    imageFleche = pygame.transform.scale(imageFleche,(30,30))
    screen.blit(textTitre, (400, 150))
    screen.blit(textStart, (400, 200))
    screen.blit(textCredits, (400, 250))
    screen.blit(textQuit, (400, 300))
    screen.blit(textHighscore,(50,50))
    if selector == 1:
        placement = 200
    elif selector == 2:
        placement = 250
    elif selector == 3:
        placement = 300
    screen.blit(imageFleche,(350, placement))
    pygame.display.update()


Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)
selector = 1
placement = 200



def draw_levels():
    windowSize = (800, 600)
    origin = (0, 0)
    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin, windowSize)
    image = pygame.Surface(windowSize)
    imageJeu = pygame.image.load("../Images/background_Menu.jpg")
    textLevelFacile = Texty.render('Facile ', 0, (255, 0, 0))
    textLevelNormal = Texty.render('Normal', 0, (255, 0, 0))
    textLevelPro = Texty.render('Pro', 0, (255, 0, 0))
    textLevelExpert = Texty.render('Expert', 0, (255, 0, 0))


    imageFleche = pygame.image.load("../Images/fleche_rouge.jpg")
    imageFleche = pygame.transform.scale(imageFleche, (30, 30))
    screen.blit(textLevelFacile, (400, 150))
    screen.blit(textLevelNormal, (400, 200))
    screen.blit(textLevelPro, (400, 250))
    screen.blit(textLevelExpert, (400, 300))

    if selector == 1:
        placement = 150
    elif selector == 2:
        placement = 200
    elif selector == 3:
        placement = 250
    elif selector == 4:
        placement = 300
    screen.blit(imageFleche, (200, placement))
    pygame.display.update()


run = True
while run:
    for event in pygame.event.get():
        drawMenu()
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
                truuuue = True
                while truuuue:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_UP:
                                if selector != 1:
                                    selector -= 1
                            elif event.key == pygame.K_DOWN:
                                if selector != 4:
                                    selector += 1
                            elif event.key == pygame.K_RETURN and selector == 1:
                                vitesse = 0.5
                                playing(vitesse)
                            elif event.key == pygame.K_RETURN and selector == 2:
                                vitesse= 1
                                playing(vitesse)
                            elif event.key == pygame.K_RETURN and selector == 3:
                                vitesse = 1.5
                                playing(vitesse)
                            elif event.key == pygame.K_RETURN and selector == 4:
                                vitesse = 2
                                playing(vitesse)
                    draw_levels()
            elif event.key == pygame.K_RETURN and selector == 2:
                drawCredits()
            elif event.key == pygame.K_RETURN and selector == 3:
                pygame.quit()
                exit()


