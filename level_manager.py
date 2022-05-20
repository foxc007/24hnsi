import random
from utils import screenutils
from sprites import enemy

class LevelManager:
    def __init__(self, game):
        self.game = game


    def run_level(self):
        for i in range(15):
            self.create_enemy()
        pass

    def create_enemy(self):
        x = random.randint(0, screenutils.get_width())
        y = screenutils.get_heigth() * 0.1
        self.game.enemy_sprites.add(enemy.Enemy(x, y))
        pass

    def on_enemy_deleted(self):
        print('adios')
        pass