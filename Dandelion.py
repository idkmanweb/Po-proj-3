import random
from Plant import Plant


class Dandelion(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 0
        self.str = 0
        self.x = x
        self.y = y
        self.name = 'd'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        world.getEntities().append(Dandelion(x, y))
        world.getMap()[x][y] = 'd'
        GUI.getLog().addBirth(self)

    def action(self, world, direction, GUI):
        for i in range(3):
            chance = (random.randint(0, 100)) % 40
            if chance == 1:
                if self.x < world.getW()-1 and world.getMap()[self.x+1][self.y] == ' ':
                    self.addBirth(world, self.x + 1, self.y, GUI)
                elif self.x > 0 and world.getMap()[self.x-1][self.y] == ' ':
                    self.addBirth(world, self.x - 1, self.y, GUI)
                elif self.y > 0 and world.getMap()[self.x][self.y-1] == ' ':
                    self.addBirth(world, self.x, self.y - 1, GUI)
                elif self.y < world.getH()-1 and world.getMap()[self.x][self.y+1] == ' ':
                    self.addBirth(world, self.x, self.y + 1, GUI)