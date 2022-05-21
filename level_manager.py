from math import log
import random
from utils import screenutils
from sprites.enemies.warrior import Warrior
from sprites.enemies.striker import Striker


class LevelManager:
    def __init__(self, game):
        self.game = game
        self.level = 1
        self.wave = 1
        self.enemies = 0

    def run_level(self):
        level = Level(self.level)
        self.waves = level.get()
        self.run_wave()

    def run_wave(self):
        wave = self.waves[self.wave-1]
        y_intervall = 74
        y = -10
        for line in wave:
            x_intervall = screenutils.get_width()-1000/len(line)
            x = 500+x_intervall/2
            for enemy in line:
                self.enemies += 1
                if enemy.startswith("s"):
                    self.game.enemy_sprites.add(
                        Striker(self.game, self, (x, y),
                                int(enemy[-1]), sync=True))
                elif enemy.startswith("w"):
                    self.game.enemy_sprites.add(
                        Warrior(self.game, self, (x, y),
                                int(enemy[-1])))
                else:
                    raise Exception("Unknown enemy type")
                x += x_intervall
            y -= y_intervall
        if len(wave) == 0:
            self.wave += 1
            self.run_wave()

    def create_enemy(self, x, y):
        self.game.enemy_sprites.add(
            Striker(self.game, self, (x, y), 3))

    def on_enemy_deleted(self):
        self.enemies -= 1
        if self.enemies == 0:
            self.wave += 1
            self.run_wave()
            if self.wave >= len(self.waves):
                self.wave = 1
                self.level += 1
                self.run_level()


class Level():
    def __init__(self, level) -> None:
        self.waves = []
        self.level = level
        for w in range(1, 4):
            self.waves.append(Wave(level, w).get())

    def get(self):
        return self.waves


class Wave():
    def __init__(self, level, rank) -> None:
        self.difficulty = int(log(level, 2)+rank)

        steps_number = int(log(self.difficulty, 2))
        self.steps = []

        enemy = random.randint(0, 1)

        # Triangle
        enemy_number = steps_number*(1+steps_number)/2
        rates = self.enemies_spawn_rates_by_tier(self.difficulty)
        enemies_by_tier = [int(
            enemy_number*rates[0]), int(enemy_number*rates[1]), int(enemy_number*rates[2])]
        if enemy == 1:
            max_rate = 0
            for j in range(3):
                if max_rate < rates[j]:
                    max_rate = rates[j]
                    max_enemy_rate = j

        for i in range(1, steps_number+1):
            for k in range(i):
                step = []
                if enemy == 0:
                    if enemies_by_tier[0] > 0:
                        step.append("warrior1")
                        enemies_by_tier[0] -= 1
                    elif enemies_by_tier[1] > 0:
                        step.append("warrior2")
                        enemies_by_tier[1] -= 1
                    elif enemies_by_tier[2] > 0:
                        step.append("warrior3")
                        enemies_by_tier[2] -= 1
                    else:
                        step.append("warrior1")
                elif enemy == 1:
                    step.append(f"striker{max_enemy_rate+1}")
                self.steps.append(step)

    def get(self):
        return self.steps

    def enemies_spawn_rates_by_tier(self, difficulty):
        if difficulty == 1:
            return [0.9, 0.2, 0.1]
        elif difficulty == 2:
            return [0.6, 0.3, 0.1]
        elif difficulty == 3:
            return [0.5, 0.4, 0.1]
        elif difficulty == 4:
            return [0.3, 0.4, 0.3]
        elif difficulty == 5:
            return [0.1, 0.4, 0.5]
        else:
            return [0, 0, 1]
