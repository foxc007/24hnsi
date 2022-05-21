import pygame
from pygame.locals import *
from utils import fileutils
import level_manager
from utils import screenutils

class Bullet(pygame.sprite.Sprite):
    def __init__(self, start_x, start_y, bullet_type):
        pygame.sprite.Sprite.__init__(self)        #Appel du constructeur de Sprite
        self.level_manager = level_manager
        self.bullet_type = bullet_type
        self.coordinates = (start_x, start_y)
        if self.bullet_type == 0:
            self.image, self.rect = fileutils.load_image('bullet.jpg')
        self.rect.topleft = self.coordinates
        screen = pygame.display.get_surface()
        

    def update(self):
        if self.bullet_type == 0:
            self.coordinates = (self.coordinates[0], self.coordinates[1] - 2)
            self.rect.topleft = self.coordinates
            if self.coordinates[1] > screenutils.get_heigth():
                self.kill()
        # Update