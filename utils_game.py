import pygame
import os


def load_image(name):
    fullname = os.path.join('assets', name)
    try:
        image = pygame.image.load(fullname)
    except pygame.error as message:
        print("Impossible de charger l'image :", name)
        raise SystemExit(message)
    image = image.convert()
    return image, image.get_rect()
