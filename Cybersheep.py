import queue
import random
from Animal import Animal
from collections import deque as queue

dRow = [-1, 0, 1, 0]
dCol = [0, 1, 0, -1]


class Cybersheep(Animal):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 4
        self.str = 11
        self.x = x
        self.y = y
        self.name = 'c'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        if world.getMap()[x][y] == ' ':
            print(world.getMap()[x][y])
            world.getEntities().append(Cybersheep(x, y))
            world.getMap()[x][y] = 'c'
            GUI.getLog().addBirth(self)
            world.sortEntities()

    def action(self, world, direction, GUI):
        vis = [[False for i in range(world.getW())] for i in range(world.getH())]
        (x,y) = self.BFS(vis, self.x, self.y, world)
        if self.x != world.getW():
            if x == world.getW() and y == world.getH():
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
            else:
                if self.x > x:
                    nx = self.x
                    ny = self.y
                    nx -= 1
                elif self.x < x:
                    nx = self.x
                    ny = self.y
                    nx += 1
                else:
                    if self.y > y:
                        nx = self.x
                        ny = self.y
                        ny -= 1
                    else:
                        nx = self.x
                        ny = self.y
                        ny += 1

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

    def isValid(self, vis, row, col, world):
        if row < 0 or col < 0 or row >= world.getW() or col >= world.getH():
            return False
        if vis[row][col]:
            return False
        return True

    def BFS(self, vis, row, col, world):
        q = queue()
        q.append((row, col))
        vis[row][col] = True

        while len(q) > 0:
            cell = q.popleft()
            x = cell[0]
            y = cell[1]

            if world.getMap()[x][y] == 'b':
                return (x,y)

            for i in range(4):
                adjx = x + dRow[i]
                adjy = y + dCol[i]
                if self.isValid(vis, adjx, adjy, world):
                    q.append((adjx, adjy))
                    vis[adjx][adjy] = True

        return (world.getW(),world.getH())
