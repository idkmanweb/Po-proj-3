import random
from Animal import Animal


class Human(Animal):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 4
        self.str = 5
        self.x = int(x)
        self.y = int(y)
        self.name = 'h'
        self.ready = 1
        self.cooldown = 0
        self.gaveBirth = 0
        self.movement = 1

    def action(self, world, direction, GUI):
        if self.x != world.getW():
            nx = self.x
            ny = self.y
            if direction == 0 and self.x > self.movement - 1:
                nx -= self.movement
            elif direction == 1 and self.x < world.getW()-self.movement:
                nx += self.movement
            elif direction == 2 and self.y > self.movement-1:
                ny -= self.movement
            elif direction == 3 and self.y < world.getH()-self.movement:
                ny += self.movement

            if self.cooldown > 7:
                self.cooldown-=1
                self.movement = 2
            elif 8 > self.cooldown > 5:
                chance =(random.randint(0 ,100)) % 2
                if chance == 0:
                    self.movement = 2
                else:
                    self.movement = 1
                self.cooldown-=1
            elif self.cooldown > 0:
                self.cooldown-=1
                self.movement = 1
            elif self.cooldown == 0:
                self.ready = 1

            if world.getMap()[nx][ny] == ' ':
                ox = self.x
                oy = self.y
                world.getMap()[nx][ny] = self.name
                world.getMap()[self.x][self.y] = ' '
                self.x = nx
                self.y = ny
            else:
                for i in world.getEntities():
                    if i.getX() == nx and i.getY() == ny and i.getName() != self.name:
                        collision = i.collision(self, world, GUI)
                        if collision == 1:
                            world.getMap()[nx][ny] = self.name
                            world.getMap()[self.x][self.y] = ' '
                            self.x = nx
                            self.y = ny
                        elif collision == 0:
                            world.getMap()[self.x][self.y] = ' '
                            self.x = world.getW()
                            self.y = world.getH()

    def addBirth(self, world, x, y, GUI):
        pass

    def getPowerReady(self):
        return self.ready

    def activatePower(self):
        if self.ready == 1:
            self.ready = 0
            self.cooldown = 9
            self.movement = 2

    def getCooldown(self):
        return self.cooldown

    def getMovement(self):
        return self.movement

    def setPowerReady(self, ready):
        self.ready = ready

    def setCooldown(self, cd):
        self.cooldown = cd

    def setMovement(self, move):
        self.movement = move