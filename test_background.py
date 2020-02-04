from movingbackground import MovingBackground
import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Test background')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((250, 250, 250))
screen.blit(background, (0, 0))
clock = pygame.time.Clock()

movingBackground = MovingBackground()
movingBackground.generateObstacles()
for obstacle in movingBackground.obstacles:
    screen.blit(obstacle.img, obstacle.pos)
pygame.display.update()

while 1:
    clock.tick(60)
    screen.blit(background, (0, 0))
    movingBackground.fall()
    for obstacle in movingBackground.obstacles:
        screen.blit(obstacle.img, obstacle.pos)
    pygame.display.update()
