from Plant import Plant


class Nightshade(Plant):

    def __init__(self, x, y):
        super().__init__(x, y)
        self.init = 0
        self.str = 99
        self.x = x
        self.y = y
        self.name = 'n'
        self.gaveBirth = 0

    def addBirth(self, world, x, y, GUI):
        world.getEntities().append(Nightshade(x, y))
        world.getMap()[x][y] = 'n'
        GUI.getLog().addBirth(self)
