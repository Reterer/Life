class Bot:
    def __init__(self, id, x, y, energy, vel, gen):
        self.id = id
        self.x = x
        self.y = y
        self.energy = energy
        self.gen = gen
        self.vel = vel
        self.color = "pink"
        self.diameter = 20

    def turn(self, world):
        return (1, 2, 6)
