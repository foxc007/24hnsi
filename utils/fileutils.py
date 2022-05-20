import os
import sys
import pygame
from pygame.locals import *


def load_image(path, colorkey=None):
    fullname = os.path.join('assets/images', path)
    try:
        image = pygame.image.load(fullname)
        if image.get_alpha() is None:
            image = image.convert()
            if colorkey is not None:
                if colorkey is -1:
                    colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        else:
            image = image.convert_alpha()
    except pygame.error as error:
        print("Impossible de charger l'image :", path)
        raise SystemExit(error.message)
    return image, image.get_rect()


def load_sound(path):
    class NoneSound:
        def play(self): pass
    if not pygame.mixer:
        return NoneSound()
    fullname = os.path.join('assets/sounds', path)
    try:
        sound = pygame.mixer.Sound(fullname)
    except pygame.error as error:
        print('Impossible de charger le son :', path)
        raise SystemExit(error.message)
    return sound
