import random
from Animal import Animal


class Antelope(Animal):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 4
        self.str = 4
        self.x = x
        self.y = y
        self.name = 'a'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        if world.getMap()[x][y] == ' ':
            print(world.getMap()[x][y])
            world.getEntities().append(Antelope(x, y))
            world.getMap()[x][y] = 'a'
            GUI.getLog().addBirth(self)
            world.sortEntities()

    def action(self, world, direction, GUI):
        if self.x != world.getW():
            dire = (random.randint(0, 100)) % 4
            nx = self.x
            ny = self.y
            if dire == 0 and self.x < world.getW() - 2:
                nx += 2
            elif dire == 1 and self.x > 1:
                nx -= 2
            elif dire == 2 and self.y > 1:
                ny -= 2
            elif dire == 3 and self.y < world.getH() - 2:
                ny += 2
            elif self.x < world.getW() - 2:
                nx += 2
            else:
                nx -= 2

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
                            chance = (random.randint(0, 100)) % 2
                            if chance == 0:
                                GUI.getLog().addKill(self, i)
                                world.getMap()[self.x][self.y] = ' '
                                self.x = world.getW()
                                self.y = world.getH()
                            else:
                                if self.x < world.getW() - 1 and world.getMap()[self.x + 1][self.y]:
                                    nx += 1
                                elif self.x > 0 and world.getMap()[self.x - 1][self.y]:
                                    nx -= 1
                                elif self.y > 0 and world.getMap()[self.x][self.y - 1]:
                                    ny -= 1
                                elif self.y < world.getH() - 1 and world.getMap()[self.x][self.y + 1]:
                                    ny += 1

    def collision(self, attacker, world, GUI):
        if attacker.getStr() >= self.str:
            self.x = world.getW()
            self.y = world.getH()
            GUI.getLog().addKill(attacker, self)
            return 1
        return 0