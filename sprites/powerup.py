import pygame
from pygame.locals import *
from utils import fileutils
import level_manager
from utils import screenutils
from random import randint


class Powerup(pygame.sprite.Sprite):
    def __init__(self, game, powerup_type):
        pygame.sprite.Sprite.__init__(self)  # Appel du constructeur de Sprite
        self.game = game
        self.powerup_type = powerup_type
        if powerup_type == 0:
            self.image, self.rect = fileutils.load_image('gati.jpg')
        elif powerup_type == 1:
            self.image, self.rect = fileutils.load_image('gato.jpg')
        self.life = options["life"]
        if list(options.keys()).count("size") > 0:
            self.rect.size = options["size"]
        else:
            self.rect.size = (64, 64)
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.rect.center = pos

    def update(self):
            self.rect.top += 10
            if self.rect.bottom > screenutils.get_heigth():
                self.kill()
                
