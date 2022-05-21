import pygame
from pygame.locals import *
from utils import fileutils
import level_manager
from utils import screenutils

class Enemy(pygame.sprite.Sprite): 
    """Enemy class"""
    def __init__(self, level_manager, start_x, start_y, enemy_type):
        pygame.sprite.Sprite.__init__(self)        #Appel du constructeur de Sprite
        self.level_manager = level_manager
        self.enemy_type = enemy_type
        self.coordinates = (start_x, start_y)
        if self.enemy_type == 0:
            self.image, self.rect = fileutils.load_image('enemy.png')
        self.rect.topleft = self.coordinates
        screen = pygame.display.get_surface()
        

    def update(self):
        if self.enemy_type == 0:
            self.coordinates = (self.coordinates[0], self.coordinates[1] + 5)
            self.rect.topleft = self.coordinates
            if self.coordinates[1] > screenutils.get_heigth():
                self.level_manager.on_enemy_deleted()
                self.kill()
        # Update