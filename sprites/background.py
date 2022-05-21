import pygame
from pygame.locals import *
from utils import fileutils

class Background(pygame.sprite.Sprite): 
    """Background class"""
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)        #Appel du constructeur de Sprite
        self.image, self.rect = fileutils.load_image("ingame_background.png")
        self.screen_width, self.screen_height = pygame.display.get_window_size()
        self.image = pygame.transform.scale(self.image, (self.screen_width, self.screen_width*2))
        self.rect.update((0,-self.screen_height),(self.screen_width, self.screen_width*2))

        self.scrolling = False
        self.speed = 1

    def start(self):
        self.scrolling = True

    def pause(self):
        self.scrolling = False

    def stop(self):
        self.scrolling = False
        self.rect.centery = 0

    def update(self):
        if self.scrolling:
            if self.rect.centery > self.screen_width:
                self.rect.centery = self.rect.centery-self.screen_width
            else:
                self.rect.centery += self.speed
        

        