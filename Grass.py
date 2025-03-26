import random
from Plant import Plant


class Grass(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 0
        self.str = 0
        self.x = x
        self.y = y
        self.name = '/'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        world.getEntities().append(Grass(x, y))
        world.getMap()[x][y] = '/'
        GUI.getLog().addBirth(self)
