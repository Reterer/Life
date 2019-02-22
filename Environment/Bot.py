class Bot:
    def __init__(self, _id, x, y, energy, vel, gen):
        self.id = _id
        self.x = x
        self.y = y
        self.energy = energy
        self.gen = gen
        self.vel = vel
        self.color = [1, 1, 0]
        self.radius = 8

    def turn(self, world):
        return (1, 2, 5)
