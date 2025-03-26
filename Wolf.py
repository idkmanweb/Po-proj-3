from Animal import Animal


class Wolf(Animal):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 5
        self.str = 9
        self.x = x
        self.y = y
        self.name = 'w'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        if world.getMap()[x][y] == ' ':
            print(world.getMap()[x][y])
            world.getEntities().append(Wolf(x, y))
            world.getMap()[x][y] = 'w'
            GUI.getLog().addBirth(self)
            world.sortEntities()
