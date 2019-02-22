from Config import *
from Environment.Bot import Bot
from Environment.Food import Food


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
            self.world = [[[0,0] for i in range(HEIGHT_MAP)] for j in
                          range(WIDTH_MAP)]  # Карта мира [x,y], все вещи имеют int координаты
        # [-1,-1] - пустота
        # [iF,-1] - еда
        # [-2,-2] - стена
        # [-1,iB] - другой бот
        if bots:
            self.bots = bots
        else:
            self.bots = [Bot(0, 5, 5, 1000, [0, 0], 0), Bot(1, 111, 111, 1000, [0, 0], 0)]
        if food:
            self.food = food
        else:
            self.food = [Food(100, 100, 12, "pink", 10)]

        for i in range(len(self.bots)):
            self.world[self.bots[i].x][self.bots[i].y] = [-1, i]
        for i in range(len(self.food)):
            self.world[self.food[i].x][self.food[i].y] = [i, -1]

    def _generate_new_food(self):
        pass

    def _collision(self, i_bot):
        x_bot, y_bot = self.bots[i_bot].x, self.bots[i_bot].y
        d_bot = self.bots[i_bot].radius
        for x in range(max(x_bot-d_bot//2, 0), min(x_bot+d_bot//2, WIDTH_MAP)):
            for y in range(max(y_bot-d_bot//2, 0), min(y_bot+d_bot//2, HEIGHT_MAP)):
                if self.world[x][y][0] > -1:
                    sq_dist = (x-self.food[self.world[x][y][0]].x)**2 + (y - self.food[self.world[x][y][0]].y)**2
                    if sq_dist <= (d_bot+self.food[self.world[x][y][0]].diameter)**2:
                        self.bots[i_bot].energy += self.food[self.world[x][y][0]].energy
                        self.world[x][y] = [-1, -1]
                        self._generate_new_food()

    def update(self):
        for i in range(len(self.bots)):
            if self.bots[i].energy <= 0:
                continue
            dx, dy, duplicate = self.bots[i].turn(self.world)
            new_vel = self.bots[i].vel

            self.bots[i].energy -= dx + dy

            if self.bots[i].energy <= 0:
                continue

            new_vel[0] += dx - new_vel[0] * F_tr
            new_vel[1] += dy - new_vel[1] * F_tr

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

            self.world[self.bots[i].x][self.bots[i].y] = [-1,-1]
            self.bots[i].x = int(x)
            self.bots[i].y = int(y)
            self.world[self.bots[i].x][self.bots[i].y] = [-1,i]

            self._collision(i)
