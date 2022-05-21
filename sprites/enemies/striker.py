import pygame
from pygame.locals import *
from sprites import bullet
from sprites.enemy import Enemy

import time
from math import sin, cos, pi
from random import randint


class Striker(Enemy):
    def __init__(self, game, level_manager, pos, tier, sync=False):
        assert tier in [1, 2, 3]
        options = {}
        options["image"] = f"enemies/striker{tier}.png"
        self.tier = tier

        if self.tier == 1:
            options["score"] = 1
            options["life"] = 1
            # Random angle mesured in gradients
            if sync:
                self.random_angle = 0
            else:
                self.random_angle = randint(0, 360) / 180 * pi

            def on_update(self):
                t = time.time()
                self.rect.x += 5*sin(t+self.random_angle)
                self.enter_screen_or_shoot()

        elif self.tier == 2:
            options["score"] = 3
            options["life"] = 3
            # Random angle mesured in gradients
            if sync:
                self.random_angle = 0
                self.rotation_direction = 1
            else:
                self.random_angle = randint(0, 360) / 180 * pi
                self.rotation_direction = randint(0, 1)
                if self.rotation_direction == 0:
                    self.rotation_direction = -1

            def on_update(self):
                t = time.time()
                if self.enter_screen_or_shoot():
                    self.rect.x += round(4*sin((t+self.random_angle)))
                    self.rect.y += round(4*cos(t+self.random_angle))

        elif self.tier == 3:
            options["score"] = 5
            options["life"] = 5
            # Random angle mesured in gradients
            if sync:
                self.random_angle = 0
                self.rotation_direction = 1
            else:
                self.random_angle = randint(0, 360) / 180 * pi
                self.rotation_direction = randint(0, 1)
                if self.rotation_direction == 0:
                    self.rotation_direction = -1

            def on_update(self):
                t = time.time()
                if self.enter_screen_or_shoot():
                    self.rect.x += round(6*sin(t+self.random_angle))
                    self.rect.y += round(4*cos(2*(t+self.random_angle)))

        options["on_update"] = on_update

        Enemy.__init__(self, game, level_manager, pos, options)

        self.base_reload_time = 5000
        self.last_shot_time = 0

    def enter_screen_or_shoot(self):
        self.reload_time = self.base_reload_time/self.game.speed_coef
        if self.rect.top < 50:
            self.rect.top += 2 * self.game.speed_coef
            return False
        else:
            if time.time() - self.last_shot_time > self.reload_time / 1000:
                self.last_shot_time = time.time()
                self.shoot()
            return True

    def shoot(self):
        self.game.enemy_bullet_sprites.add(
            bullet.Bullet(self.game, self.rect.centerx, self.rect.bottom, 1))
