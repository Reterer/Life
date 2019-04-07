import numpy as np
import math
import Environment.ActivationFunc as af


class Bot:

    def __init__(self, _id, x, y, energy, vel):
        self.id = _id
        self.x = x
        self.y = y
        self.energy = energy
        self.vel = vel
        self.color = [255, 0, 0]
        self.radius = 10
        self.eat_food = 0

        # Гены
        self.eyes_count = 12  # Кол-во глаз
        self.raycast_d = 2  # Шаг рэйкаста - чем меньше, тем более точно, но более медленно
        self.raycast_distans = 60  # Как далеко идет луч

        # Нейронка
        self.l1 = 5  # Кол-во выходных нейронов первого слоя
        self.l2 = 3  # Кол-во выходных нейронов второго слоя

        self.W_1 = (np.random.random((self.eyes_count*3 + 1, self.l1)) - 0.5) * 5
        self.b_1 = (np.random.random(self.l1) - 0.5) * 2

        self.W_2 = (np.random.random((self.l1, self.l2)) - 0.5) * 5
        self.b_2 = (np.random.random(self.l2) - 0.5) * 2

    def __str__(self):
        return "bot id: {} | energy: {:.3f} | eat: {}".format(self.id, self.energy, self.eat_food)

    def _predict(self, data):
        y1 = af.relu(np.matmul(data, self.W_1) + self.b_1)
        y2 = (af.sigmoid(np.matmul(y1, self.W_2) + self.b_2) - 0.5) * 2
        res = list(y2)
        res[2] = int((res[2] + 1) / 2 + 0.3)
        #  print(res, data)
        return res

    def turn(self, world, food, bots):

        mini_map = world[max(self.x - self.raycast_distans, 0): min(self.x + self.raycast_distans, len(world))]
        for x in range(len(mini_map)):
            mini_map[x] = mini_map[x][
                          max(self.y - self.raycast_distans, 0): min(self.y + self.raycast_distans, len(mini_map[x]))]
        for y in range(len(mini_map[0])):
            for x in range(len(mini_map)):
                if mini_map[x][y][0] == 1:
                    r = mini_map[x][y][2]
                    for _x in range(max(x - r, 0), min(x + r, len(mini_map))):
                        for _y in range(max(y - r, 0), min(y + r, len(mini_map[x]))):
                            mini_map[_x][_y] = [1, 0, 0]

        data = [0 for _ in range(self.eyes_count*3 + 1)]
        alpha = 6.28 / self.eyes_count

        x_on_minimap = self.x - max(self.x - self.raycast_distans, 0)
        y_on_minimap = self.y - max(self.y - self.raycast_distans, 0)
        for i in range(self.eyes_count):
            ray = [math.cos(alpha * i), math.sin(alpha * i)]
            di = self.raycast_d
            while di < self.raycast_distans:
                x = int(ray[0] * di + x_on_minimap)
                y = int(ray[1] * di + y_on_minimap)
                # print(x,y)
                if 0 <= x < len(mini_map) and 0 <= y < len(mini_map[0]):
                    _a = 1 / di
                    if mini_map[x][y][0] == 1:
                        data[i * 3] = food[mini_map[x][y][1]].color[0] * _a
                        data[i * 3 + 1] = food[mini_map[x][y][1]].color[1] * _a
                        data[i * 3 + 2] = food[mini_map[x][y][1]].color[2] * _a
                        break
                    elif mini_map[x][y][0] == 3:
                        data[i * 3 + 2] = 255 * _a
                        break
                di += self.raycast_d
        return self._predict(data)
