import pygame
from pygame.locals import *
from utils import fileutils
import level_manager
from utils import screenutils
from random import randint


class Enemy(pygame.sprite.Sprite):
    """Enemy class"""

    def __init__(self, game, level_manager, pos, options: dict):
        pygame.sprite.Sprite.__init__(self)  # Appel du constructeur de Sprite
        self.game = game
        self.level_manager = level_manager
        self.on_update = options["on_update"]
        self.image, self.rect = fileutils.load_image(options["image"])
        self.life = options["life"]
        if list(options.keys()).count("size") > 0:
            self.rect.size = options["size"]
        else:
            self.rect.size = (64, 64)
        self.image = pygame.transform.scale(self.image, self.rect.size)
        self.rect.center = pos

    def hit(self, power=1):
        self.life -= power
        if self.life <= 0:
            self.delete()

    def delete(self):
        self.game.score += 1
        self.level_manager.on_enemy_deleted()
        self.kill()
        pygame.mixer.Sound.play(self.game.alien_death_sounds[randint(
            0, len(self.game.alien_death_sounds)-1)])

    def update(self):
        self.on_update(self)
        # Update
