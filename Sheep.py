from Animal import Animal


class Sheep(Animal):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 4
        self.str = 4
        self.x = x
        self.y = y
        self.name = 's'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        if world.getMap()[x][y] == ' ':
            print(world.getMap()[x][y])
            world.getEntities().append(Sheep(x, y))
            world.getMap()[x][y] = 's'
            GUI.getLog().addBirth(self)
            world.sortEntities()
