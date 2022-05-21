import pygame
from pygame.locals import *
from utils import fileutils
import level_manager
from utils import screenutils
from random import randint


class Powerup(pygame.sprite.Sprite):
    def __init__(self, game, powerup_type, pos):
        pygame.sprite.Sprite.__init__(self)  # Appel du constructeur de Sprite
        self.game = game
        self.powerup_type = powerup_type
        self.image, self.rect = fileutils.load_image('powerup.png')
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.rect.center = pos

    def update(self):
            self.rect.top += 10
            if self.rect.bottom > screenutils.get_heigth():
                self.kill()
                
