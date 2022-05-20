import os
import sys
import pygame
import random
from pygame.locals import *
from enemy import Enemy

if not pygame.font:
    print('Attention, polices désactivées')
if not pygame.mixer:
    print('Attention, son désactivé')


def main():
    global running
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
    enemy_sprites = pygame.sprite.Group()
    clock = pygame.time.Clock()
    running = True

    def handle_events():
        global running
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False

    def logic():
        main_sprites.update()
        enemy_sprites.update()

    def render():
        screen.blit(background, (0, 0))
        main_sprites.draw(screen)
        enemy_sprites.draw(screen)
        pygame.display.flip()

    x = random.randint(0, width)
    y = height * 0.1

    enemy_sprites.add(Enemy(x, y))

    while running:
        clock.tick(60)
        handle_events()
        logic()
        render()


if __name__ == '__main__':
    main()
    sys.exit()
