import numpy as np

RADIUS_VISION = 200 #Не вытаскивай, это временно

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class Bot:
    def __init__(self, _id, x, y, energy, vel, gen):
        self.id = _id
        self.x = x
        self.y = y
        self.energy = energy
        self.gen = gen
        self.vel = vel
        self.color = "pink"
        self.diameter = 20
        self.is_alive = True

        self.h = 5
        self.l1 = 4
        self.out = 3

        self.W_1 = (np.random.random((self.h, self.l1)) - 0.5) * 2
        self.b_1 = (np.random.random(self.l1) - 0.5) * 2

        self.W_2 = (np.random.random((self.l1, self.out)) - 0.5) * 2
        self.b_2 = (np.random.random(self.out) - 0.5) * 2

    def network_predict(self, data):
        #print(data)
        y_1 = np.matmul(data, self.W_1) + self.b_1
        y_2 = sigmoid(np.matmul(y_1, self.W_2) + self.b_2)
        y_2[2] = int(y_2[2] + 0.3)
        print(y_2)
        return y_2

    def turn(self, world):
        lu_v, ru_v, ld_v, rd_v = 0, 0, 0, 0
        for x in range(max(0, self.x-RADIUS_VISION), min(len(world), self.x+RADIUS_VISION)):
            for y in range(max(0, self.y-RADIUS_VISION), min(len(world[0]), self.y+RADIUS_VISION)):
                if world[x][y][0] > -1:
                    if (x - self.x < 0) and (y - self.y < 0):
                        lu_v += 1/((self.x - x)**2 + (self.y - y)**2)

                    elif (x - self.x > 0) and (y - self.y < 0):
                        ru_v += 1/((self.x - x)**2 + (self.y - y)**2)

                    elif (x - self.x < 0) and (y - self.y > 0):
                        ld_v += 1/((self.x - x)**2 + (self.y - y)**2)

                    elif (x - self.x > 0) and (y - self.y > 0):
                        rd_v += 1/((self.x - x)**2 + (self.y - y)**2)
        data = [lu_v, ru_v, ld_v, rd_v, self.energy]

        return self.network_predict(data)
