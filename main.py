import os
import sys
import pygame
from pygame.locals import *

if not pygame.font:
    print('Attention, polices désactivées')
if not pygame.mixer:
    print('Attention, son désactivé')

# Initialisation de pygame
pygame.init()
screenInfos = pygame.display.Info()
width = screenInfos.current_w
height = screenInfos.current_h

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Space invaders')
pygame.mouse.set_visible(0)
