import pygame
from pygame.locals import *
from utils.fileutils import load_image, load_sound


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface):
        pygame.sprite.Sprite.__init__(self)
        self.image, self.rect = load_image('spaceship.png')
        self.screen_size = screen.get_size()
        self.rect.centerx = self.screen_size[0] / 2
        self.rect.y = self.screen_size[1]*5//6
        self.speed = 10

    def update(self, keys_pressed: list):
        if not (K_LEFT in keys_pressed and K_RIGHT in keys_pressed):
            if K_LEFT in keys_pressed:
                self.move_left()
            elif K_RIGHT in keys_pressed:
                self.move_right()

    def move_right(self):
        if self.rect.right + self.speed > self.screen_size[0]:
            self.rect.right = self.screen_size[0]
        else:
            self.rect.right += self.speed

    def move_left(self):
        if self.rect.left - self.speed < 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def shoot(self):
        pass
