from Config import *
from Bot import Bot
import random


class Environment:
    def __init__(self):
        # self._setup()
        pass

    def setup(self, filename=None):
        if filename:
            pass
        else:
            self._setup()

    def _setup(self, world=None, bots=None, food=None):
        if world:
            self.world = world
        else:
            self.world = [[-1 for i in range(HEIGHT_MAP)] for j in
                          range(WIDTH_MAP)]  # Карта мира [x,y], все вещи имеют int координаты
        # -1 - пустота
        # -2 - еда
        # -3 - стена
        # id - другой бот
        if bots:
            self.bots = bots
        else:
            self.bots = [Bot(0, 10, 10, 50, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0), Bot(1, 20, 20, 100, [0, 0], 0)]

        if food:
            self.food = food
        else:
            self.food = [[1, 10], [20, 14]]

    def update(self):
        for i in range(len(self.bots)):
            dx, dy, duplicate = self.bots[i].turn(self.world)
            newVel = self.bots[i].vel

            self.bots[i].energy -= dx + dy

            newVel[0] += dx - newVel[0] * 0.1
            newVel[1] += dy - newVel[1] * 0.1

            x = self.bots[i].x + newVel[0] * DELTA_TIME
            y = self.bots[i].y + newVel[1] * DELTA_TIME

            if x >= WIDTH_MAP:
                x = WIDTH_MAP - 1
                newVel[0] = 0
            if x < 0:
                x = 0
                newVel[0] = 0
            if y >= HEIGHT_MAP:
                y = HEIGHT_MAP - 1
                newVel[1] = 0
            if y < 0:
                y = 0
                newVel[1] = 0

            self.bots[i].vel[0] = newVel[0]
            self.bots[i].vel[1] = newVel[1]

            self.world[self.bots[i].x][self.bots[i].y] = -1
            self.bots[i].x = int(x)
            self.bots[i].y = int(y)
            self.world[self.bots[i].x][self.bots[i].y] = i
