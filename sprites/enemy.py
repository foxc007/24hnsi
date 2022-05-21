import pygame
from pygame.locals import *
from utils import fileutils
import level_manager
from utils import screenutils
from random import randint
from sprites import powerup


class Enemy(pygame.sprite.Sprite):
    """Enemy class"""

    def __init__(self, game, level_manager, pos, options: dict):
        pygame.sprite.Sprite.__init__(self)  # Appel du constructeur de Sprite
        self.game = game
        self.score = options["score"]
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
            if randint(0, 25) <= self.score:
                self.game.powerup_sprites.add(powerup.Powerup(self.game, randint(0, 1), self.rect.center))
            self.delete()
        else:
            pygame.mixer.Sound.play(pygame.mixer.Sound(f'assets/sounds/alien_degat{randint(1, 5)}.ogg'))

    def delete(self):
        self.game.score += self.score
        self.level_manager.on_enemy_deleted()
        self.kill()
        pygame.mixer.Sound.play(self.game.alien_death_sounds[randint(0, len(self.game.alien_death_sounds)-1)])

    def update(self):
        self.on_update(self)
        # Update
