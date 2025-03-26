import random
from Entity import Entity


class Plant(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.str = 0
        self.x = x
        self.y = y
        self.name = ' '
        self.init = 0
        self.gaveBirth = 0

    def action(self, world, direction, GUI):
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

    def collision(self, attacker, world, GUI):
        if attacker.getStr() >= self.str:
            self.x = world.getW()
            self.y = world.getH()
            GUI.getLog().addFood(attacker, self)
            return 1
        GUI.getLog().addKill(self, attacker)
        return 0

    def getBirth(self):
        return self.gaveBirth

    def setBirth(self, yes):
        self.gaveBirth = yes

    def addBirth(self, world, x, y, GUI):
        pass
