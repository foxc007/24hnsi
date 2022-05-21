import pygame
from pygame.locals import *
from utils.fileutils import load_image, load_sound
import time
from sprites import bullet


class Spaceship(pygame.sprite.Sprite):
    def __init__(self, screen: pygame.Surface, game):
        pygame.sprite.Sprite.__init__(self)
        self.game = game
        self.image, self.rect = load_image('spaceship.png')
        self.screen_size = screen.get_size()
        self.rect.centerx = self.screen_size[0] / 2
        self.rect.y = self.screen_size[1]*5//6
        self.speed = 10
        self.last_shot_time = 0

    def update(self, keys_pressed: list):
        self.time_between_shots = 1000
        if not (K_LEFT in keys_pressed and K_RIGHT in keys_pressed):
            if K_LEFT in keys_pressed:
                self.move_left()
            elif K_RIGHT in keys_pressed:
                self.move_right()
        if K_SPACE in keys_pressed and time.time() - self.last_shot_time > self.time_between_shots / 1000:
            self.last_shot_time = time.time()
            self.shoot()

    def move_right(self):
        if self.rect.right + self.speed > self.screen_size[0]:
            self.rect.right = self.screen_size[0]
        else:
            self.rect.right += self.speed

    def move_left(self):
        if self.rect.left - self.speed < 0:
            self.rect.left = 0
        else:
            self.rect.left -= self.speed

    def shoot(self):
        self.game.bullet_sprites.add(bullet.Bullet(self.game,
                                                  self.rect.centerx, self.rect.top, 0))
