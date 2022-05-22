import pygame
from pygame.locals import *
from utils import fileutils


class Background(pygame.sprite.Sprite):
    """Background class"""

    def __init__(self, game):
        self.game = game
        pygame.sprite.Sprite.__init__(self)  # Appel du constructeur de Sprite
        self.image, self.rect = fileutils.load_image("ingame_background.png")
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        self.image = pygame.transform.scale(
            self.image, (self.screen_width, self.screen_width*16))
        self.rect.update((0, - 8 * self.screen_width),
                         (self.screen_width, self.screen_width*16))

        self.scrolling = False


    def start(self):
        self.scrolling = True

    def pause(self):
        self.scrolling = False

    def stop(self):
        self.scrolling = False
        self.rect.centery = 0

    def update(self):
        self.speed = 2 * self.game.speed_coef
        if self.scrolling:
            if self.rect.centery > 8 * self.screen_width:
                self.rect.centery = self.rect.centery - 8 * self.screen_width
            else:
                self.rect.centery += self.speed
