import random

class Bot:
    def __init__(self, _id, x, y, energy, vel):
        self.id = _id
        self.x = x
        self.y = y
        self.energy = energy
        self.vel = vel
        self.color = [1, 1, 0]
        self.radius = 8
        self.eat_food = 0

    def turn(self, world):
        if random.randint(0, 100) == 0:
            return 0.1, 0.2, 1
        return 0.3, 0.2, 0
