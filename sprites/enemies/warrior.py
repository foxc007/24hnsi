import pygame
from pygame.locals import *
from sprites.enemy import Enemy


class Warrior(Enemy):
    def __init__(self, game, level_manager, pos, tier):
        assert tier in [1, 2, 3]
        options = {}
        options["image"] = f"warrior${tier}.png"
        if tier == 1:
            options["life"] = 1

        def on_update(self):
            self.rect.top += 1
        options["on_update"] = on_update
        Enemy.__init__(game, level_manager, pos, options)
