import os
import sys
import pygame
import random
from pygame.locals import *
from sprites.spaceship import Spaceship
from sprites.enemy import Enemy
from sprites.background import Background
import level_manager

if not pygame.font:
    print('Attention, polices désactivées')
if not pygame.mixer:
    print('Attention, son désactivé')


class Game:
    def __init__(self):
        pygame.init()
        screenInfos = pygame.display.Info()
        self.width = screenInfos.current_w
        self.height = screenInfos.current_h

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Space invaders')
        pygame.mouse.set_visible(0)
        self.speed_coef = 1

        self.background = Background(self)
        self.background.start()
        self.screen.blit(self.background.image, self.background.rect)
        pygame.display.flip()

        #pygame.mixer.init()
        #self.music_intro = pygame.mixer.music.load('assets/sounds/debut_musique.ogg')
        #pygame.mixer.music.play(self.music_intro)


        self.main_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.spaceship = Spaceship(self.screen, self)
        self.spaceship.add(self.main_sprites)

        self.clock = pygame.time.Clock()

        self.level_manager = level_manager.LevelManager(self)
        self.level_manager.run_level()

        self.keys_pressed = []

        self.running = True

        while self.running:
            self.clock.tick(60)
            self.handle_events()
            self.logic()
            self.render()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                self.keys_pressed.append(event.key)
            elif event.type == KEYUP:
                self.keys_pressed.remove(event.key)

    def logic(self):
        self.spaceship.update(self.keys_pressed)
        self.background.update()
        self.enemy_sprites.update()

    def render(self):
        self.screen.blit(self.background.image, self.background.rect)
        self.main_sprites.draw(self.screen)
        self.bullet_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    Game()
    sys.exit()
