import os
import sys
import pygame
import random
from pygame.locals import *
from sprites.enemy import Enemy
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

        self.background = pygame.Surface(self.screen.get_size())
        #self.background = self.background.convert()
        #self.background = self.background.fill((250, 250, 250))

        self.screen.blit(self.background, (0, 0))
        pygame.display.flip()

        self.main_sprites = pygame.sprite.Group()
        self.enemy_sprites = pygame.sprite.Group()
        self.clock = pygame.time.Clock()
        self.level_manager = level_manager.LevelManager(self)
        self.level_manager.run_level()
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

    def logic(self):
        self.main_sprites.update()
        self.enemy_sprites.update()

    def render(self):
        self.screen.blit(self.background, (0, 0))
        self.main_sprites.draw(self.screen)
        self.enemy_sprites.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    Game().__init__()
    sys.exit()