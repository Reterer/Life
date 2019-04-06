import random
import numpy as np
from Config import *
from Environment.Bot import Bot
from Environment.Food import Food
from prettytable import PrettyTable


class Environment:
    def __init__(self):
        # self._setup()
        pass

    def setup(self, filename=None):
        if filename:
            pass
        else:
            self._setup()

    def _setup(self, world=None, bots=None, food=None, epoch=0, iter_for_epoch=500, crt_iter=0):
        self.epoch = epoch
        self.iter_for_epoch = iter_for_epoch
        self.crt_iter = crt_iter

        self.generator_id_bot = 2

        if world:
            self.world = world
        else:
            self.world = [[[0, None, None] for i in range(HEIGHT_MAP)] for j in
                          range(WIDTH_MAP)]  # Карта мира [x,y], все вещи имеют int координаты
        # [0,None,None] - пустота
        # [1,Food_index,radius] - еда
        # [2,Bot_index,radius] - Бот
        # [3,None,None] - Стена
        if bots:
            self.bots = bots
        else:
            def generate_bot(i):
                for i in range(i):
                    x, y = random.randint(0, WIDTH_MAP - 1), random.randint(0, HEIGHT_MAP - 1)
                    while self.world[x][y][0] != 0:
                        x, y = random.randint(0, WIDTH_MAP - 1), random.randint(0, HEIGHT_MAP - 1)
                    self.world[x][y] = [0, i, 8]
                    yield Bot(i, x, y, 1000, [0, 0])

            self.bots = [bot for bot in generate_bot(20)]
        if food:
            self.food = food
        else:
            def generate_food(i):
                for i in range(i):
                    x, y = random.randint(0, WIDTH_MAP - 1), random.randint(0, HEIGHT_MAP - 1)
                    while self.world[x][y][0] != 0:
                        x, y = random.randint(0, WIDTH_MAP - 1), random.randint(0, HEIGHT_MAP - 1)
                    self.world[x][y] = [1, i, 3]
                    yield Food(x, y, 5, [1, 0, 1], 100)

            self.food = [food for food in generate_food(50)]

        for i in range(len(self.bots)):
            self.world[self.bots[i].x][self.bots[i].y] = [2, i, self.bots[i].radius]
        for i in range(len(self.food)):
            self.world[self.food[i].x][self.food[i].y] = [1, i, self.food[i].radius]

    #  Вызывается, когда бот ест еду
    def _generate_new_food(self, id_food):
        x = self.food[id_food].x
        y = self.food[id_food].y
        self.world[x][y] = [0, None, None]
        x = random.randint(0, WIDTH_MAP-1)
        y = random.randint(0, HEIGHT_MAP-1)
        while self.world[x][y][0] != 0:
            x = random.randint(0, WIDTH_MAP-1)
            y = random.randint(0, HEIGHT_MAP-1)
        self.world[x][y] = [1, id_food, self.food[id_food].radius]
        self.food[id_food].x = x
        self.food[id_food].y = y

    #  Взаимодействие ботов с окружающей средой

    def _collision(self, i_bot):
        x_bot, y_bot = self.bots[i_bot].x, self.bots[i_bot].y
        r_bot = self.bots[i_bot].radius
        for x in range(max(x_bot - 2 * r_bot, 0), min(x_bot + 2 * r_bot, WIDTH_MAP)):
            for y in range(max(y_bot - 2 * r_bot, 0), min(y_bot + 2 * r_bot, HEIGHT_MAP)):
                if self.world[x][y][0] == 1:
                    sq_dist = (x - x_bot) ** 2 + (y - y_bot) ** 2
                    if sq_dist < (r_bot + self.food[self.world[x][y][1]].radius) ** 2:
                        self.bots[i_bot].energy += self.food[self.world[x][y][1]].energy
                        self.bots[i_bot].eat_food += 1
                        self._generate_new_food(self.world[x][y][1])

    def new_bot(self, in_bot):
        x = in_bot.x
        y = in_bot.y
        energy = in_bot.energy
        vel = [in_bot.vel[0], in_bot.vel[1]]
        color = in_bot.color
        radius = in_bot.radius

        bot = Bot(0, x, y, energy, vel)
        bot.color = color
        bot.radius = radius
        bot.id = self.generator_id_bot
        self.generator_id_bot += 1

        bot.W_1 = np.copy(in_bot.W_1)
        bot.W_2 = np.copy(in_bot.W_2)
        bot.b_1 = np.copy(in_bot.b_1)
        bot.b_2 = np.copy(in_bot.b_2)

        return bot

    def _mutation(self, bot):
        rnd = random.randint(0, 3)
        if rnd == 0:
            bot.W_1 += (np.random.random((bot.eyes_count + 1, bot.l1)) - 0.5) * 0.2
        elif rnd == 1:
            bot.W_2 += (np.random.random((bot.l1, bot.l2)) - 0.5) * 0.2
        elif rnd == 2:
            bot.b_1 += (np.random.random(bot.l1) - 0.5) * 0.2
        else:
            bot.b_2 += (np.random.random(bot.l2) - 0.5) * 0.2

    def _generate_bots(self, id_bot):
        a_bot = self.new_bot(self.bots[id_bot])
        b_bot = self.new_bot(self.bots[id_bot])
        if a_bot.x > 0:
            a_bot.x -= 1
        else:
            a_bot.x += 1

        a_bot.energy /= 2
        a_bot.energy *= 0.8
        if a_bot.energy < 10:
            a_bot.energy = 0

        b_bot.energy /= 2
        b_bot.energy *= 0.8
        if b_bot.energy < 10:
            b_bot.energy = 0

        a_bot.vel[0] *= 2
        a_bot.vel[1] *= 2
        b_bot.vel[0] *= -1
        b_bot.vel[1] *= -1

        # rnd = random.randint(0, 99)
        # if rnd < 5:
        #    if random.randint(0, 1) == 0:
        #        self._mutation(a_bot)
        #    else:
        #        self._mutation(b_bot)

        return a_bot, b_bot

    def _die_bot(self, i):
        self.world[self.bots[i].x][self.bots[i].y] = [0, None, None]
        self.bots.pop(i)

    def update(self):
        self.crt_iter += 1
        if self.crt_iter % 10 == 0:
            print(self.crt_iter, self.epoch)
        #  Переход на новую эпоху
        if self.crt_iter == self.iter_for_epoch:
            print(self.crt_iter, self.epoch)
            self.epoch += 1
            self.crt_iter = 0

            t = PrettyTable(['#', 'Score'])
            new_bots = sorted(self.bots, key=lambda bot: bot.eat_food, reverse=True)

            for i in range(len(new_bots)):
                t.add_row([i, new_bots[i].eat_food])
            print(t)

            for bot in new_bots:
                self.world[bot.x][bot.y] = [0, None, None]

            new_bots = new_bots[:min(20, len(new_bots))]
            if len(new_bots) < 10:
                new_bots += new_bots
            len_bots = len(new_bots)
            if len_bots > 0:
                #  Получение новых ботов
                a = new_bots[:int(len_bots * 0.4)]
                random.shuffle(new_bots)
                b_1 = new_bots[:int(len_bots * 0.3)]
                random.shuffle(new_bots)
                b_2 = new_bots[:int(len_bots * 0.3)]
                random.shuffle(new_bots)
                c = new_bots[:int(len_bots * 0.3)]

                #  Скрещивание ботов
                b = []
                for pair in zip(b_1, b_2):
                    W_1 = np.copy(pair[random.randint(0, 1)].W_1)
                    W_2 = np.copy(pair[random.randint(0, 1)].W_2)
                    B_1 = np.copy(pair[random.randint(0, 1)].b_1)
                    B_2 = np.copy(pair[random.randint(0, 1)].b_2)
                    b.append(Bot(pair[0].id, pair[0].x, pair[0].y, 1000, [0, 0]))
                    b[-1].W_1 = W_1
                    b[-1].W_2 = W_2
                    b[-1].b_1 = B_1
                    b[-1].b_2 = B_2

                for i in range(len(c)):
                    self._mutation(c[i])
                new_bots = a + b + c

                for i in range(len(new_bots)):
                    x_bot, y_bot = random.randint(0, WIDTH_MAP - 1), random.randint(0, HEIGHT_MAP - 1)
                    while self.world[x_bot][y_bot][0] != 0:
                        x_bot, y_bot = random.randint(0, WIDTH_MAP - 1), random.randint(0, HEIGHT_MAP - 1)
                    new_bots[i].x = x_bot
                    new_bots[i].y = y_bot
                    self.world[x_bot][y_bot] = [2, bot.id, bot.radius]
                    new_bots[i] = self.new_bot(new_bots[i])

                random.shuffle(new_bots)
                self.bots = new_bots
            else:
                pass

        i = 0
        while i < len(self.bots):
            # print(len(self.bots), i, self.bots[i].energy)
            if self.bots[i].energy <= 0:
                self._die_bot(i)
                continue

            dx, dy, duplicate = self.bots[i].turn(self.world)
            if duplicate == 1:
                bot_a, bot_b = self._generate_bots(i)
                self.bots[i] = bot_a
                self.bots.append(bot_b)
            else:
                new_vel = self.bots[i].vel
                self.bots[i].energy -= dx + dy

                if self.bots[i].energy <= 0:
                    self._die_bot(i)
                    continue

                new_vel[0] += dx - new_vel[0] * F_tr * DELTA_TIME
                new_vel[1] += dy - new_vel[1] * F_tr * DELTA_TIME

                x = self.bots[i].x + new_vel[0] * DELTA_TIME
                y = self.bots[i].y + new_vel[1] * DELTA_TIME

                if x >= WIDTH_MAP:
                    x = WIDTH_MAP - 1
                    new_vel[0] = 0
                if x < 0:
                    x = 0
                    new_vel[0] = 0
                if y >= HEIGHT_MAP:
                    y = HEIGHT_MAP - 1
                    new_vel[1] = 0
                if y < 0:
                    y = 0
                    new_vel[1] = 0

                self.bots[i].vel[0] = new_vel[0]
                self.bots[i].vel[1] = new_vel[1]

                self.world[self.bots[i].x][self.bots[i].y] = [0, None, None]
                self.bots[i].x = int(x)
                self.bots[i].y = int(y)
                self.world[self.bots[i].x][self.bots[i].y] = [2, i, self.bots[i].radius]

                self._collision(i)
            i += 1
