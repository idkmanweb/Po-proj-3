import random
from Entity import Entity


class Animal(Entity):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.str = 0
        self.x = x
        self.y = y
        self.name = ' '
        self.init = 0
        self.gaveBirth = 0

    def action(self, world, direction, GUI):
        if self.x != world.getW():
            dire = (random.randint(0, 100)) % 4
            nx = self.x
            ny = self.y
            if dire == 0 and self.x < world.getW() - 1:
                nx += 1
            elif dire == 1 and self.x > 0:
                nx -= 1
            elif dire == 2 and self.y > 0:
                ny -= 1
            elif dire == 3 and self.y < world.getH() - 1:
                ny += 1
            elif self.x < world.getW() - 1:
                nx += 1
            else:
                nx -= 1

            if world.getMap()[nx][ny] == ' ':
                world.getMap()[nx][ny] = self.name
                world.getMap()[self.x][self.y] = ' '
                ox = self.x
                oy = self.y
                self.x = nx
                self.y = ny
            elif world.getMap()[nx][ny] == self.name:
                print(world.getMap()[nx][ny])
                isOK = 1
                for i in world.getEntities():
                    if i.getX() == nx and i.getY() == ny:
                        isOK = i.getBirth()
                if self.gaveBirth == 0 and isOK == 0:
                    if nx < world.getW() - 1 and world.getMap()[nx + 1][ny] == ' ':
                        self.addBirth(world, nx + 1, ny, GUI)
                        self.gaveBirth = 1
                        for j in world.getEntities():
                            if j.getX() == nx and j.getY() == ny:
                                j.setBirth(1)
                            if j.getX() == nx + 1 and j.getY() == ny:
                                j.setBirth(1)

                elif nx > 0 and world.getMap()[nx - 1][ny] == ' ':
                    self.addBirth(world, nx - 1, ny, GUI)
                    self.gaveBirth = 1
                    for i in world.getEntities():
                        if i.getX() == nx and i.getY() == ny:
                            i.setBirth(1)

                        if i.getX() == nx - 1 and i.getY() == ny:
                            i.setBirth(1)

                elif ny < world.getH() - 1 and world.getMap()[nx][ny + 1] == ' ':
                    self.addBirth(world, nx, ny + 1, GUI)
                    self.gaveBirth = 1
                    for i in world.getEntities():
                        if i.getX() == nx and i.getY() == ny:
                            i.setBirth(1)
                        if i.getX() == nx and i.getY() == ny + 1:
                            i.setBirth(1)
                elif ny > 0 and world.getMap()[nx][ny - 1] == ' ':
                    self.addBirth(world, nx, ny - 1, GUI)
                    self.gaveBirth = 1
                    for i in world.getEntities():
                        if i.getX() == nx and i.getY() == ny:
                            i.setBirth(1)
                        if i.getX() == nx and i.getY() == ny - 1:
                            i.setBirth(1)
                world.sortEntities()
            else:
                this = self
                for i in world.getEntities():
                    if i.getX() == nx and i.getY() == ny and self.name != i.getName():
                        print(this, i)
                        collision = i.collision(this, world, GUI)
                        if collision == 1:
                            if self.x != world.getW():
                                world.getMap()[nx][ny] = self.name
                                world.getMap()[self.x][self.y] = ' '
                                self.x = nx
                                self.y = ny
                        elif collision == 0:
                            world.getMap()[self.x][self.y] = ' '
                            self.x = world.getW()
                            self.y = world.getH()

    def collision(self, attacker, world, GUI):
        if attacker.getStr() >= self.str:
            self.x = world.getW()
            self.y = world.getH()
            GUI.getLog().addKill(attacker, self)
            return 1
        GUI.getLog().addKill(self, attacker)
        return 0

    def getBirth(self):
        return self.gaveBirth

    def setBirth(self, yes):
        self.gaveBirth = yes

    def addBirth(self, world, x, y, GUI):
        pass
