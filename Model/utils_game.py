import pygame

PATH = "../Images/"


def load_image(name):
    image = pygame.image.load(name)
    return image.convert_alpha()


def scale_image(image, width, height):
    return pygame.transform.smoothscale(image, (width, height)).convert_alpha()
