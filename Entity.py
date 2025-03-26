from abc import ABC


class Entity(ABC):

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.name = ' '
        self.str = 0
        self.init = 0

    def collision(self, attacker, world, GUI):
        pass

    def action(self, world, direction, GUI):
        pass

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def getInit(self):
        return self.init

    def getStr(self):
        return self.str

    def getName(self):
        return self.name

    def getIcon(self):
        return self.icon

    def getPowerReady(self):
        pass

    def getCooldown(self):
        pass

    def getMovement(self):
        pass

    def setPowerReady(self, ready):
        pass

    def setCooldown(sel, cd):
        pass

    def setMovement(self, move):
        pass

    def activatePower(self):
        pass

    def ateGuarana(self):
        self.str += 3
