import pygame
import random


class BackgroundAnime(pygame.sprite.Sprite):
    def __init__(self, images):
        super(BackgroundAnime, self).__init__()

        size = (800, 600)
        self.images = images
        self.rect = pygame.Rect((0, 0), size)
        self.index = 0
        self.image = self.images[self.index]

        self.animation_time = 0.09
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

        self.speed = 1

    def update_time_dependent(self, dt):
        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(0, 0)

    def update_frame_dependent(self):
        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(0, 0)

    def update(self, dt):
        # Switch between the two update methods by commenting/uncommenting.
        self.update_time_dependent(dt)
        # self.update_frame_dependent()
