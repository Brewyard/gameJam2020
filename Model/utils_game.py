import pygame

PATH = "../Images/"


def load_image(name):
    image = pygame.image.load(name)
    return image


def scale_image(image, width, height):
    return pygame.transform.smoothscale(image, (width, height))
