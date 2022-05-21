import pygame
from pygame.locals import *
from sprites.enemy import Enemy
from utils import screenutils


class Warrior(Enemy):
    def __init__(self, game, level_manager, pos, tier):
        assert tier in [1, 2, 3]
        options = {}
        options["image"] = f"enemies/warrior{tier}.png"
        options["life"] = tier

        def on_update(self):
            self.rect.top += 1
            if self.rect.bottom > screenutils.get_heigth():
                self.level_manager.on_enemy_deleted()
                self.kill()
                self.game.remove_health()
        options["on_update"] = on_update
        Enemy.__init__(self, game, level_manager, pos, options)
