import pygame
from pygame.locals import *
from utils import fileutils

class Enemy(pygame.sprite.Sprite): 
    """Enemy class"""
    def __init__(self, start_x, start_y):
        pygame.sprite.Sprite.__init__(self)        #Appel du constructeur de Sprite
        self.coordinates = (start_x, start_y)
        self.image, self.rect = fileutils.load_image('testsquare.png', -1)
        screen = pygame.display.get_surface()
        

    def update(self):
        pass
        # Update