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
        self.base_speed = 10
        self.inertia = 0
        self.base_reload_time = 1000
        self.last_shot_time = 0
        self.powerups = []

    def update(self, keys_pressed: list):
        self.speed = self.base_speed*self.game.speed_coef
        self.reload_time = self.base_reload_time/self.game.speed_coef

        if not (K_LEFT in keys_pressed and K_RIGHT in keys_pressed):
            if K_LEFT in keys_pressed:
                if self.inertia > -self.speed:
                    self.inertia -= 0.75
            elif K_RIGHT in keys_pressed:
                if self.inertia < self.speed:
                    self.inertia += 0.75
            else:
                self.inertia = self.inertia/1.1
            self.move()
        else:
            self.inertia = self.inertia/1.1
            self.move()


        if K_SPACE in keys_pressed and time.time() - self.last_shot_time > self.reload_time / 1000:
            self.last_shot_time = time.time()
            self.shoot()
        hit = False
        for bullet_collided in pygame.sprite.spritecollide(self, self.game.enemy_bullet_sprites, False):
            bullet_collided.kill()
            hit = True
            break

        for powerup_collided in pygame.sprite.spritecollide(self, self.game.powerup_sprites, False):
            bullet_collided.kill()
            hit = True
            break
        if hit:
            self.game.remove_health()

    def move(self):
        if self.rect.centerx + self.inertia > self.screen_size[0]:
            self.rect.left = 0
        elif self.rect.centerx - self.inertia < 0:
            self.rect.right = self.screen_size[0]
        else:
            self.rect.centerx += round(self.inertia)

    def shoot(self):
        self.game.bullet_sprites.add(bullet.Bullet(self.game,self.rect.centerx, self.rect.top, 0))
        pygame.mixer.Sound.play(pygame.mixer.Sound(f'assets/sounds/shoot_sound.ogg'))
