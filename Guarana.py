import random
from Plant import Plant


class Guarana(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 0
        self.str = 0
        self.x = x
        self.y = y
        self.name = 'g'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        world.getEntities().append(Guarana(x, y))
        world.getMap()[x][y] = 'g'
        GUI.getLog().addBirth(self)

    def collision(self, attacker, world, GUI):
        self.x = world.getW()
        self.y = world.getH()
        GUI.getLog().addFood(attacker, self)
        attacker.ateGuarana()
        return 1
