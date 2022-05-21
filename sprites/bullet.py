import pygame
from pygame.locals import *
from utils import fileutils
import level_manager
from utils import screenutils


class Bullet(pygame.sprite.Sprite):
    def __init__(self, game, start_x, start_y, bullet_type):
        pygame.sprite.Sprite.__init__(self)  # Appel du constructeur de Sprite
        self.game = game
        self.level_manager = level_manager
        self.bullet_type = bullet_type
        if self.bullet_type == 0:
            self.image, self.rect = fileutils.load_image(
                'bullet.jpg', colorkey=-1)
            self.rect.size = (50, 50)
            self.image = pygame.transform.scale(
                self.image, (self.rect.width, self.rect.height))
        self.rect.centerx, self.rect.bottom = start_x, start_y+30
        screen = pygame.display.get_surface()

    def update(self):
        if self.bullet_type == 0:
            self.rect.top -= 10
            if self.rect.top < 0:
                self.kill()
        hit = False
        for enemy_hit in pygame.sprite.spritecollide(self, self.game.enemy_sprites, False):
            enemy_hit.delete()
            hit = True
        if hit:
            self.kill()
        # Update
