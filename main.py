import os
import sys
import pygame
from pygame.locals import *
from enemy import Enemy

if not pygame.font:
    print('Attention, polices désactivées')
if not pygame.mixer:
    print('Attention, son désactivé')

enemies = []

def main():
    # Initialisation de pygame
    pygame.init()
    screenInfos = pygame.display.Info()
    width = screenInfos.current_w
    height = screenInfos.current_h

    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Space invaders')
    pygame.mouse.set_visible(0)

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))

    screen.blit(background, (0, 0))
    pygame.display.flip()

    main_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()

    running = True

    def render():
        screen.blit(background, (0, 0))
        main_sprites.draw(screen)
        pygame.display.flip()

    create_enemy(200, 200)

    while running:
        clock.tick(60)
        render()

def create_enemy(start_x, start_y):
    enemies.append(Enemy(start_x, start_y))
    main_sprites.add(Enemy(start_x, start_y))

if __name__ == '__main__':
    main()
