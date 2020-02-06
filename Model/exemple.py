import pygame
pygame.init()

SIZE = WIDTH, HEIGHT = 720, 480
BACKGROUND_COLOR = pygame.Color('black')
FPS = 60
PATH = "../Images/"

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

def load_image(name):
    image = pygame.image.load(name)
    return image


def load_images():
    #images = [load_image(PATH + "bubble.png"), load_image(PATH + "bubble75horizon.png"), load_image(PATH + "bubble50horizon.png"),
    #          load_image(PATH + "bubble75horizon.png"), load_image(PATH + "bubble.png"), load_image(PATH + "bubble75verti.png"),
    #          load_image(PATH + "bubble50verti.png"), load_image(PATH + "bubble75verti.png")]
    images = [load_image(PATH + "vent2.png"), load_image(PATH + "vent3.png"),
              load_image(PATH + "vent4.png"), load_image(PATH + "vent5.png"), load_image(PATH + "vent6.png"),
              load_image(PATH + "vent7.png"), load_image(PATH + "vent8.png")]
              #load_image(PATH + "vent9.png"),
              #load_image(PATH + "vent10.png"), load_image(PATH + "vent11.png"), load_image(PATH + "vent12.png"),
              #load_image(PATH + "vent13.png"), load_image(PATH + "vent14.png"), load_image(PATH + "vent15.png"),
              #load_image(PATH + "vent16.png")]
    #images = [load_image(PATH + "bird_blue_1.png"), load_image(PATH + "bird_blue_2.png"), load_image(PATH + "bird_blue_3.png")]
    #images = [load_image(PATH + "bird_brown_1.png"), load_image(PATH + "bird_brown_2.png"), load_image(PATH + "bird_brown_3.png")]
    #images = [load_image(PATH + "bird_robin_1.png"), load_image(PATH + "bird_robin_2.png"), load_image(PATH + "bird_robin_3.png")]
    #images = [load_image(PATH + "bubbles_group_1.png"), load_image(PATH + "bubbles_group_2.png"), load_image(PATH + "bubbles_group_3.png"),
    #          load_image(PATH + "bubbles_group_4.png"), load_image(PATH + "bubbles_group_5.png")]
    #images = [load_image(PATH + "wind-sens-1.png"), load_image(PATH + "wind-sens-2.png"), load_image(PATH + "wind-sens-3.png")]
    #images = [load_image(PATH + "frame_00.png"), load_image(PATH + "frame_01.png"), load_image(PATH + "frame_02.png"),
    #          load_image(PATH + "frame_03.png"), load_image(PATH + "frame_04.png"), load_image(PATH + "frame_05.png"),
    #          load_image(PATH + "frame_06.png"), load_image(PATH + "frame_07.png"), load_image(PATH + "frame_08.png"),
    #          load_image(PATH + "frame_09.png"), load_image(PATH + "frame_10.png"), load_image(PATH + "frame_11.png"),
    #          load_image(PATH + "frame_12.png"), load_image(PATH + "frame_13.png"), load_image(PATH + "frame_14.png")]
    #images = [load_image(PATH + "wind1.png"), load_image(PATH + "wind2.png"), load_image(PATH + "wind3.png"), load_image(PATH + "wind4.png")]
    return images


class AnimatedSprite(pygame.sprite.Sprite):

    def __init__(self, position, images):
        super(AnimatedSprite, self).__init__()

        size = (64, 64)  # This should match the size of the images.

        self.rect = pygame.Rect(position, size)
        self.images = images
        self.images_right = images
        self.images_left = [pygame.transform.flip(image, True, False) for image in images]  # Flipping every image.
        self.index = 0
        self.image = images[self.index]  # 'image' is the current image of the animation.

        self.velocity = pygame.math.Vector2(0, 0)

        self.animation_time = 0.1
        self.current_time = 0

        self.animation_frames = 6
        self.current_frame = 0

    def update_time_dependent(self, dt):
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_time += dt
        if self.current_time >= self.animation_time:
            self.current_time = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update_frame_dependent(self):
        if self.velocity.x > 0:  # Use the right images if sprite is moving right.
            self.images = self.images_right
        elif self.velocity.x < 0:
            self.images = self.images_left

        self.current_frame += 1
        if self.current_frame >= self.animation_frames:
            self.current_frame = 0
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]

        self.rect.move_ip(*self.velocity)

    def update(self, dt):
        # Switch between the two update methods by commenting/uncommenting.
        self.update_time_dependent(dt)
        # self.update_frame_dependent()


def main():
    images = load_images()  # Make sure to provide the relative or full path to the images directory.
    player = AnimatedSprite(position=(50, 50), images=images)
    all_sprites = pygame.sprite.Group(player)  # Creates a sprite group and adds 'player' to it.

    running = True
    while running:

        dt = clock.tick(FPS) / 1000  # Amount of seconds between each loop.

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    player.velocity.x = 4
                elif event.key == pygame.K_LEFT:
                    player.velocity.x = -4
                elif event.key == pygame.K_DOWN:
                    player.velocity.y = 4
                elif event.key == pygame.K_UP:
                    player.velocity.y = -4
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                    player.velocity.x = 0
                elif event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                    player.velocity.y = 0

        all_sprites.update(dt)  # Calls the 'update' method on all sprites in the list (currently just the player).

        screen.fill(BACKGROUND_COLOR)
        all_sprites.draw(screen)
        pygame.display.update()


if __name__ == '__main__':
    main()
