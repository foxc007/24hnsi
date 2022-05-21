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
import time

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
        self.last_music_change = 0
        self.last_button_change = time.time()
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
            fileutils.load_sound('alien_sound.ogg'))

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

        self.images = {}
        self.images["bullet"] = fileutils.load_image("bullet.png")
        self.images["simple_enemy_bullet"] = fileutils.load_image(
            "simple_enemy_bullet.png")

        pygame.mixer.init()
        pygame.mixer.music.load('assets/sounds/debut_musique.ogg')
        pygame.mixer.music.play()
        pygame.mixer.music.queue('assets/sounds/loop_musique.ogg', 'ogg', -1)
        self.music = 0

        self.main_sprites = pygame.sprite.Group()
        self.bullet_sprites = pygame.sprite.Group()
        self.powerup_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.enemy_bullet_sprites = pygame.sprite.Group()
        self.spaceship = Spaceship(self.screen, self)
        self.spaceship.add(self.main_sprites)

        self.clock = pygame.time.Clock()

        self.menu_opened = True
        self.menu_button_selected = 0

        
        self.keys_pressed = []

        self.running = True
        self.font = pygame.font.SysFont(None, 48)
        self.has_played = False
        while self.running:
            self.clock.tick(60)
            self.handle_events()
            if not self.menu_opened:
                self.logic()
                self.render()
            else:
                self.menu()
                
                
    def menu(self):

        if self.menu_button_selected == 0:
            pygame.draw.rect(self.screen,(0,255,0),(200,500,500,80))
            pygame.draw.rect(self.screen,(128,128,128),(710,500,500,80))
            pygame.draw.rect(self.screen,(128,128,128),(1220,500,500,80))
        elif self.menu_button_selected == 1:
            pygame.draw.rect(self.screen,(128,128,128),(200,500,500,80))
            pygame.draw.rect(self.screen,(0,255,0),(710,500,500,80))
            pygame.draw.rect(self.screen,(128,128,128),(1220,500,500,80))
        else:
            pygame.draw.rect(self.screen,(128,128,128),(200,500,500,80))
            pygame.draw.rect(self.screen,(128,128,128),(710,500,500,80))
            pygame.draw.rect(self.screen,(0,255,0),(1220,500,500,80))
        button1 = self.font.render('Play', True, (0,0,0))
        button2 = self.font.render('Change music', True, (0,0,0))
        button3 = self.font.render('Quit game', True, (0,0,0))
        self.screen.blit(button1, (415, 525))
        self.screen.blit(button2, (825, 525))
        self.screen.blit(button3, (1380, 525))

        if self.has_played:
            hp_text = self.font.render('YOU DEAD, SCORE = ' + str(self.score), True, (245, 14, 78))
            self.screen.blit(hp_text, (self.width / 2 - 100, self.height / 2 + 50))
        pygame.display.flip()

        if not (K_RIGHT in self.keys_pressed and K_LEFT in self.keys_pressed):

            if K_RIGHT in self.keys_pressed and time.time() - self.last_button_change > 0.2:
                self.last_button_change = time.time()
                if self.menu_button_selected < 2:
                    self.menu_button_selected += 1
                else:
                    self.menu_button_selected = 0
            elif K_LEFT in self.keys_pressed and time.time() - self.last_button_change > 0.2:
                self.last_button_change = time.time()
                if self.menu_button_selected > 0:
                    self.menu_button_selected -= 1
                else:
                    self.menu_button_selected = 2
            
            elif K_SPACE in self.keys_pressed or K_RETURN in self.keys_pressed:
                if self.menu_button_selected == 0:
                    self.menu_opened = False
                    self.run_game()
                elif self.menu_button_selected == 1:
                    if K_RETURN in self.keys_pressed and time.time() - self.last_music_change > 0.5:
                        self.last_music_change = time.time()
                        self.switch_music()
                else:
                    pygame.quit()

    def run_game(self):
        self.health = 3
        self.score = 0
        self.enemy_sprites.empty()
        self.enemy_bullet_sprites.empty()
        self.level_manager = level_manager.LevelManager(self)
        self.level_manager.run_level()
        self.switch_music()
        self.has_played = True


    def switch_music(self):
        if self.music == 0:
            pygame.mixer.music.unload()
            pygame.mixer.music.load('assets/sounds/musique_2.ogg')
            pygame.mixer.music.play()
            self.music = 1
        else:
            pygame.mixer.music.unload()
            pygame.mixer.music.load('assets/sounds/debut_musique.ogg')
            pygame.mixer.music.play()
            pygame.mixer.music.queue('assets/sounds/loop_musique.ogg')
            self.music = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False

                if event.key == K_RETURN and time.time() - self.last_music_change > 5:
                    self.last_music_change = time.time()
                    self.switch_music()
                self.keys_pressed.append(event.key)
            elif event.type == KEYUP:
                if event.key in self.keys_pressed:
                    self.keys_pressed.remove(event.key)

    def logic(self):
        self.spaceship.update(self.keys_pressed)
        self.background.update()
        self.bullet_sprites.update()
        self.powerup_sprites.update()
        self.enemy_sprites.update()
        self.enemy_bullet_sprites.update()

    def remove_health(self):
        self.health = self.health - 1
        if self.health <= 0:
            pygame.mixer.Sound.play(pygame.mixer.Sound(self.player_death))
            pygame.draw.rect(self.screen,(128,128,128),(180,20,150,30))
            self.menu_opened = True
            self.keys_pressed = []

    def render(self):
        self.screen.blit(self.background.image, self.background.rect)

        hp_text = self.font.render(
            'HP : ' + str(self.health), True, (245, 14, 78))
        pygame.draw.rect(self.screen, (128, 128, 128), (180, 20, 150, 30))
        pygame.draw.rect(self.screen, (0, 255, 0), (180, 20, 50*self.health, 30))

        self.screen.blit(hp_text, (20, 20))

        score_text = self.font.render('Score : ' + str(self.score), True, (245, 14, 78))
        self.screen.blit(score_text, (20, 60))
        self.main_sprites.draw(self.screen)
        self.bullet_sprites.draw(self.screen)
        self.powerup_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        self.enemy_bullet_sprites.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    Game()
    sys.exit()
