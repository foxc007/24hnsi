import pygame
from pygame.locals import *
from sprites import bullet
from sprites.enemy import Enemy

import time
from math import sin, pi
from random import randint


class Striker(Enemy):
    def __init__(self, game, level_manager, pos, tier, sync=False):
        assert tier in [1, 2, 3]
        options = {}
        options["image"] = f"enemies/striker{tier}.png"
        options["life"] = tier
        self.tier = tier

        if self.tier == 1:
            # Random angle mesured in gradients
            if sync:
                angle = 0
            else:
                self.random_angle = randint(0, 360) / 180 * pi

            def on_update(self):
                t = time.time()
                self.rect.x += 5*sin(t+self.random_angle)
                self.enter_screen_or_shoot()

        options["on_update"] = on_update
        Enemy.__init__(self, game, level_manager, pos, options)

        self.base_reload_time = 5000
        self.last_shot_time = 0

    def enter_screen_or_shoot(self):
        self.reload_time = self.base_reload_time/self.game.speed_coef
        if self.rect.top < 50:
            self.rect.top += 1 * self.game.speed_coef
        else:
            if time.time() - self.last_shot_time > self.reload_time / 1000:
                self.last_shot_time = time.time()
                self.shoot()

    def shoot(self):
        self.game.enemy_bullet_sprites.add(
            bullet.Bullet(self.game, self.rect.centerx, self.rect.bottom, 1))
