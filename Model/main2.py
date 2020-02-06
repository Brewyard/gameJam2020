import pygame
from credits import drawCredits
from main import playing
from game import Game
from main import gameOver

pygame.init()
Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)
selector = 1
placement = 200
game = Game()
selectorLevels = 1
selectorMenu = 1
music_Menu = pygame.mixer.Sound('../Sounds/Otarie.wav')

f = open('../highscore.txt', 'r')
highscore = int(f.read())
f.close()

def drawMenu():
    #Generer la fenetre de notre jeu
    windowSize = (800, 600)
    origin = (0,0)
    global highscore
    global selectorMenu
    placement = 200
    pygame.display.set_caption('Le Menu')
    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin,windowSize)
    image = pygame.Surface(windowSize)
    imageJeu = pygame.image.load("../Images/background_Menu.jpg")
    textTitre = Texty.render('Bubble Escape ', 0, (255, 0, 0))
    textStart = Texty.render('Start', 0, (255, 0, 0))
    textCredits = Texty.render('Credits', 0, (255, 0, 0))
    textQuit = Texty.render('Quit ', 0, (255, 0, 0))
    textHighscore = Texty.render("Highscore : "+str(highscore),0,(255,0,0))
    imageFleche = pygame.image.load("../Images/fleche_rouge.jpg")
    imageFleche = pygame.transform.scale(imageFleche,(30,30))
    screen.blit(textTitre, (300, 150))
    screen.blit(textStart, (300, 200))
    screen.blit(textCredits, (300, 250))
    screen.blit(textQuit, (300, 300))
    screen.blit(textHighscore,(50,50))
    if selectorMenu == 1:
        placement = 200
    elif selectorMenu == 2:
        placement = 250
    elif selectorMenu == 3:
        placement = 300
    screen.blit(imageFleche,(260, placement))
    pygame.display.update()



def draw_levels():
    Texty = pygame.font.Font('../Images/SUPERPOI_R.TTF', 20)
    Textyy = pygame.font.Font('../Images/SUPERPOI_R.TTF', 10)
    placement = 200
    global selectorLevels
    windowSize = (800, 600)
    origin = (0, 0)
    pygame.display.set_caption('Les Niveaux')
    screen = pygame.display.set_mode(windowSize)
    rect = pygame.Rect(origin, windowSize)
    image = pygame.Surface(windowSize)
    imageJeu = pygame.image.load("../Images/background_Menu.jpg")
    textLevelFacile = Texty.render('Facile ', 0, (255, 0, 0))
    textLevelNormal = Texty.render('Normal', 0, (255, 0, 0))
    textLevelPro = Texty.render('Pro', 0, (255, 0, 0))
    textLevelExpert = Texty.render('Expert', 0, (255, 0, 0))
    textLevelRetour= Texty.render('Retour', 0, (0, 255, 0))

    imageFleche = pygame.image.load("../Images/fleche_rouge.jpg")
    imageFleche = pygame.transform.scale(imageFleche, (30, 30))
    screen.blit(textLevelFacile, (300, 150))
    screen.blit(textLevelNormal, (300, 200))
    screen.blit(textLevelPro, (300, 250))
    screen.blit(textLevelExpert, (300, 300))
    screen.blit(textLevelRetour, (300, 350))

    if selectorLevels == 1:
        placement = 150
    elif selectorLevels == 2:
        placement = 200
    elif selectorLevels == 3:
        placement = 250
    elif selectorLevels == 4:
        placement = 300
    elif selectorLevels ==5:
        placement = 350
    screen.blit(imageFleche, (260, placement))
    pygame.display.update()




music_Menu.play()
run = True
while run:
    for event in pygame.event.get(): ########boucle du menu
        drawMenu()
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if selectorMenu != 1:
                    selectorMenu -= 1
            elif event.key == pygame.K_DOWN:
                if selectorMenu != 3:
                    selectorMenu += 1
            elif event.key == pygame.K_RETURN and selectorMenu == 1: #####On choisit de jouer => levels
                truuuue = True
                quitter = False
                while truuuue:
                    for e in pygame.event.get():
                        if e.type == pygame.QUIT:
                            pygame.quit()
                            exit()
                        elif e.type == pygame.KEYDOWN:
                            if e.key == pygame.K_UP:
                                if selectorLevels != 1:
                                    selectorLevels -= 1
                            elif e.key == pygame.K_DOWN:
                                if selectorLevels != 5:
                                    selectorLevels += 1
                            elif e.key == pygame.K_RETURN and selectorLevels == 1: #on a choisit le niveau facile, tant que l'on joue rien sinon game over
                                music_Menu.stop()
                                vitesse = 0.5
                                res = playing(vitesse)
                                if not res: ##on arrive sur la page game over si jeu finit
                                    gameOver()
                                    break
                                         #  ici direction draw_levels
                            elif e.key == pygame.K_RETURN and selectorLevels == 2:
                                music_Menu.stop()
                                vitesse= 1
                                res = playing(vitesse)
                            elif e.key == pygame.K_RETURN and selectorLevels == 3:
                                music_Menu.stop()
                                vitesse = 1.5
                                res = playing(vitesse)
                            elif e.key == pygame.K_RETURN and selectorLevels == 4:
                                music_Menu.stop()
                                vitesse = 2
                                res = playing(vitesse)
                            elif e.key == pygame.K_RETURN and selectorLevels == 5:
                                music_Menu.stop()
                                quitter = True
                                break

                    draw_levels()
                    if quitter:
                        quitter = False
                        break

            elif event.key == pygame.K_RETURN and selectorMenu == 2: #bouton credits
                drawCredits()
            elif event.key == pygame.K_RETURN and selectorMenu == 3: #bouton quit
                pygame.quit()
                exit()


