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
        if tier == 1:
            options["score"] = 1
        elif tier == 2:
            options["score"] = 3
        elif tier == 3:
            options["score"] = 5

        def on_update(self):
            if self.rect.top < 50:
                self.rect.top += 2 * self.game.speed_coef
            else:
                self.rect.top += 1 * self.game.speed_coef
            if self.rect.bottom > screenutils.get_heigth():
                self.level_manager.on_enemy_deleted()
                self.kill()
                self.game.remove_health()
        options["on_update"] = on_update
        Enemy.__init__(self, game, level_manager, pos, options)
