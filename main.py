import os
import sys
import pygame
import random
from pygame.locals import *
from sprites.spaceship import Spaceship
from sprites.enemy import Enemy
from sprites.background import Background
import level_manager
from utils import fileutils, screenutils

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
        self.score = 0

        self.running = True
        self.font = pygame.font.SysFont(None, 48)

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
                if event.key in self.keys_pressed:
                    self.keys_pressed.remove(event.key)

    def logic(self):
        self.spaceship.update(self.keys_pressed)
        self.background.update()
        self.bullet_sprites.update()
        self.enemy_sprites.update()
        self.enemy_bullet_sprites.update()

    def remove_health(self):
        self.health = self.health - 1
        if self.health <= 0:
            local_running = True
            while local_running:
                self.clock.tick(60)
                for event in pygame.event.get():
                    if event.type == QUIT:
                        self.running = False
                        local_running = False
                    elif event.type == KEYDOWN:
                        if event.key == K_ESCAPE:
                            self.running = False
                            local_running = False
                        if event.key == K_SPACE:
                            local_running = False
                hp_text = self.font.render('YOU DEAD, SCORE = ' + str(self.score), True, (245, 14, 78))
                self.screen.blit(hp_text, (self.width / 2, self.height / 2))
                pygame.display.flip()
            self.health = 3
            self.score = 0


    def render(self):
        self.screen.blit(self.background.image, self.background.rect)

        hp_text = self.font.render('HP : ' + str(self.health), True, (245, 14, 78))
        self.screen.blit(hp_text, (20, 20))

        score_text = self.font.render('Score : ' + str(self.score), True, (245, 14, 78))
        self.screen.blit(score_text, (20, 60))
        self.main_sprites.draw(self.screen)
        self.bullet_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        self.enemy_bullet_sprites.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    Game()
    sys.exit()
