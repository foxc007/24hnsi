import os
import sys
import pygame
import random
from pygame.locals import *
from sprites.spaceship import Spaceship
from sprites.enemy import Enemy
from sprites.background import Background
import level_manager
from utils import fileutils

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

        self.alien_death_sounds = []
        self.alien_death_sounds.append(
            fileutils.load_sound('alien_death1.ogg'))
        self.alien_death_sounds.append(
            fileutils.load_sound('alien_death2.ogg'))
        self.alien_death_sounds.append(
            fileutils.load_sound('alien_death3.ogg'))
        self.alien_death_sounds.append(
            fileutils.load_sound('alien_death4.ogg'))
        self.alien_death_sounds.append(
            fileutils.load_sound('alien_death5.ogg'))

        self.alien_death_sounds = []
        self.alien_death_sounds.append(
            fileutils.load_sound('alien_sound1.ogg'))
        self.alien_death_sounds.append(
            fileutils.load_sound('alien_sound2.ogg'))

        self.boss_music = fileutils.load_sound('boss_music.ogg')

        self.menu_sound = fileutils.load_sound('menu_sound.ogg')

        self.player_death = fileutils.load_sound('player_death.ogg')

        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Space invaders')
        pygame.mouse.set_visible(0)
        self.speed_coef = 1

        self.background = Background(self)
        self.background.start()
        self.screen.blit(self.background.image, self.background.rect)
        pygame.display.flip()

        pygame.mixer.init()
        pygame.mixer.music.load('assets/sounds/debut_musique.ogg')
        pygame.mixer.music.play()
        pygame.mixer.music.queue('assets/sounds/loop_musique.ogg', 'ogg', -1)

        self.main_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_bullet_sprites = pygame.sprite.Group()
        self.spaceship = Spaceship(self.screen, self)
        self.spaceship.add(self.main_sprites)

        self.clock = pygame.time.Clock()

        self.level_manager = level_manager.LevelManager(self)
        self.level_manager.run_level()

        self.keys_pressed = []

        self.health = 3

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
        self.bullet_sprites.update()
        self.enemy_sprites.update()
        self.enemy_bullet_sprites.update()

    def remove_health(self):
        self.health - + 1
        if self.health == 0:
            font = pygame.font.Font(None, 36)
            text = font.render(
                "Pummel The Chimp, And Win $$$", 1, (10, 10, 10))
            textpos = text.get_rect(centerx=self.background.get_width()/2)
            self.background.blit(text, textpos)

    def render(self):
        self.screen.blit(self.background.image, self.background.rect)
        self.main_sprites.draw(self.screen)
        self.bullet_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        self.enemy_bullet_sprites.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    Game()
    sys.exit()
