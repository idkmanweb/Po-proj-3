import random
import numpy
from Antelope import Antelope
from Borscht import Borscht
from Cybersheep import Cybersheep
from Dandelion import Dandelion
from Fox import Fox
from Grass import Grass
from Guarana import Guarana
from Human import Human
from Nightshade import Nightshade
from Sheep import Sheep
from Turtle import Turtle
from Wolf import Wolf


class World:

    def __init__(self, w, h, GUI):
        self.turn = 0
        self.numberOfEntities = 0
        self.height = h
        self.width = w
        self.entities = []
        self.map = [[' ' for i in range(w)] for j in range(h)]
        tempx = int((random.randint(0, 100)) % self.width)
        tempy = int((random.randint(0, 100)) % self.height)
        self.entities.append(Human(self.width / 2, self.height / 2))
        self.map[int(self.width / 2)][int(self.height / 2)] = self.entities[self.numberOfEntities].getName()
        self.numberOfEntities += 1
        while self.map[tempx][tempy] != ' ':
            tempx = int((random.randint(0, 100)) % self.width)
            tempy = int((random.randint(0, 100)) % self.height)
        self.entities.append(Cybersheep(tempx, tempy))
        self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
        self.numberOfEntities += 1
        for i in range(int((self.width * self.height) / 100 - 1)):
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Sheep(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Borscht(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Antelope(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Dandelion(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Fox(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Grass(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Guarana(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Nightshade(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Turtle(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1
            while self.map[tempx][tempy] != ' ':
                tempx = int((random.randint(0, 100)) % self.width)
                tempy = int((random.randint(0, 100)) % self.height)
            self.entities.append(Wolf(tempx, tempy))
            self.map[tempx][tempy] = self.entities[self.numberOfEntities].getName()
            self.numberOfEntities += 1

    def doTurn(self, GUI, direction):
        if direction != -1:
            self.turn += 1
            GUI.getLog().addTurn(self.turn)
            for i in self.entities:
                if i.getX() != self.width and i.getY() != self.height:
                    i.action(self, direction, GUI)
            for i in self.entities:
                i.setBirth(0)
            for i in self.entities:
                if i.getX() == self.width:
                    del i
            self.entities.sort(key=lambda x: x.getInit(), reverse=True)
            GUI.clear()
            GUI.update(self)
            GUI.getLog().clear()

    def getMap(self):
        return self.map

    def getEntities(self):
        return self.entities

    def getW(self):
        return self.width

    def getH(self):
        return self.height

    def getTurn(self):
        return self.turn

    def setEntities(self, vector):
        self.entities = vector

    def clear(self):
        self.map = None
        self.entities = None
        self.entities = numpy.array(list)

    def loadMap(self, w, h, t, size):
        self.width = w
        self.height = h
        self.turn = t
        self.numberOfEntities = size

    def addLoadedEntity(self, org):
        self.entities.append(org)

    def sortEntities(self):
        self.entities.sort(key=lambda x: x.getInit(), reverse=True)

    def generateMap(self):
        self.map = [[' ']*self.height]*self.width
        for i in range(0, len(self.entities) - 1):
            self.map[self.entities[i].getX()][self.entities[i].getY()] = self.entities[i].getName()
