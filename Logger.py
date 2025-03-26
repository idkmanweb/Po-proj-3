

class Logger:

    def __init__(self):
        self.log = ""

    def addKill(self, attacker, prey):
        self.log += '\n'
        self.log += attacker.getName()
        self.log += " zabil "
        self.log += prey.getName()
        self.log += " w ("
        self.log += str(attacker.getX())
        self.log += ","
        self.log += str(attacker.getY())
        self.log += ")"

    def addFood(self, animal, food):
        self.log += "\n"
        self.log += animal.getName()
        self.log += " zjadl "
        self.log += food.getName()
        self.log += " w ("
        self.log += str(animal.getX())
        self.log += ","
        self.log += str(animal.getY())
        self.log += ")"

    def addBirth(self, animal):
        self.log += "\n"
        self.log += animal.getName()
        self.log += " urodzil sie w ("
        self.log += str(animal.getX())
        self.log += ","
        self.log += str(animal.getY())
        self.log += ")"

    def addPlant(self, plant):
        self.log += "\n"
        self.log += plant.getName()
        self.log += " rozpylil sie w ("
        self.log += str(plant.getX())
        self.log += ","
        self.log += str(plant.getY())
        self.log += ")"

    def addTurn(self, turn):
        self.log += " -- Tura "
        self.log += str(turn)
        self.log += " --"

    def write(self):
        return self.log

    def clear(self):
        self.log = ""
