import random
from Animal import Animal
from Plant import Plant


class Borscht(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 0
        self.str = 10
        self.x = x
        self.y = y
        self.name = 'b'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        world.getEntities().append(Borscht(x, y))
        world.getMap()[x][y] = 'b'
        GUI.getLog().addBirth(self)


    def action(self, world, direction, GUI):
        chance = (random.randint(0, 100)) % 40
        if chance == 1:
            if self.x < world.getW()-1 and world.getMap()[self.x+1][self.y] == ' ':
                self.addBirth(world, self.x+1, self.y, GUI)
            elif self.x > 0 and world.getMap()[self.x-1][self.y] == ' ':
                self.addBirth(world, self.x-1, self.y, GUI)
            elif self.y > 0 and world.getMap()[self.x][self.y-1] == ' ':
                self.addBirth(world, self.x, self.y-1, GUI)
            elif self.y < world.getH()-1 and world.getMap()[self.x][self.y+1] == ' ':
                self.addBirth(world, self.x, self.y+1, GUI)

        if self.x < world.getW() - 1 and world.getMap()[self.x + 1][self.y] != 'b' and world.getMap()[self.x + 1][self.y] != ' ' and world.getMap()[self.x + 1][self.y] != 'c':
            for i in world.getEntities():
                 if i.getX() == self.x+1 and i.getY() == self.y and issubclass(i.__class__, Animal):
                    collision = i.collision(self, world, GUI)
                    if collision == 1:
                        world.getMap()[self.x + 1][self.y] = ' '
                    break
        if self.x > 0 and world.getMap()[self.x - 1][self.y] != 'b' and world.getMap()[self.x - 1][self.y] != ' ' and world.getMap()[self.x - 1][self.y] != 'c':
            for i in world.getEntities():
                if i.getX() == self.x-1 and i.getY() == self.y and issubclass(i.__class__, Animal):
                    collision = i.collision(self, world, GUI)
                    if collision == 1:
                        world.getMap()[self.x - 1][self.y] = ' '
                    break
        if self.y < world.getH() - 1 and world.getMap()[self.x][self.y + 1] != 'b' and world.getMap()[self.x][self.y + 1] != ' ' and world.getMap()[self.x][self.y + 1] != 'c':
            for i in world.getEntities():
                if i.getX() == self.x and i.getY() == self.y + 1 and issubclass(i.__class__, Animal):
                    collision = i.collision(self, world, GUI)
                    if collision == 1:
                        world.getMap()[self.x][self.y + 1] = ' '
                    break
        if self.x > 0 and world.getMap()[self.x][self.y - 1] != 'b' and world.getMap()[self.x][self.y - 1] != ' ' and world.getMap()[self.x][self.y - 1] != 'c':
            for i in world.getEntities():
                if i.getX() == self.x and i.getY() == self.y - 1 and issubclass(i.__class__, Animal):
                    collision = i.collision(self, world, GUI)
                    if collision == 1:
                        world.getMap()[self.x][self.y - 1] = ' '
                    break
