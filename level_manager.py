import random
from utils import screenutils
from sprites.enemies.warrior import Warrior
from sprites.enemies.striker import Striker


class LevelManager:
    def __init__(self, game):
        self.game = game
        self.enemies = 0

    def run_level(self):
        for i in range(3):
            self.create_enemy()
            self.enemies += 1
        if (self.game.speed_coef < 3):
            self.game.speed_coef += 0.1
        pass

    def create_enemy(self):
        x = random.randint(500, screenutils.get_width()-500)
        y = -screenutils.get_heigth() * 0.05
        self.game.enemy_sprites.add(
            Striker(self.game, self, (x, y), 2))

    def on_enemy_deleted(self):
        self.enemies -= 1
        if self.enemies == 0:
            self.run_level()
