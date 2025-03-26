from Human import Human
from World import World
from GUI import GUI
import pygame
import pickle
from Start import Start

width = 20
height = 20
start = Start()

while start.isReady() == 0:
    pass

tmpwidth, tmpheight = start.returnWH()

if tmpwidth > 0 and tmpheight > 0:
    width = tmpwidth
    height = tmpheight

del start

GUI1 = GUI(width, height)
world = World(width, height, GUI1)

GUI1.update(world)
GUI1.clear()

while GUI1.getRun():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            GUI1.setRun(0)

        pressed = pygame.key.get_pressed()
        if pressed[pygame.K_UP]:
            world.doTurn(GUI1, 2)
        elif pressed[pygame.K_DOWN]:
            world.doTurn(GUI1, 3)
        elif pressed[pygame.K_LEFT]:
            world.doTurn(GUI1, 0)
        elif pressed[pygame.K_RIGHT]:
            world.doTurn(GUI1, 1)
        elif pressed[pygame.K_p]:
            for i in world.getEntities():
                if isinstance(i, Human):
                    i.activatePower()
                    break
        elif pressed[pygame.K_s]:
            filename = "save.pkl"
            print("save")
            with open(filename, 'wb') as file:
                print("save2")
                pickle.dump(world, file)
        elif pressed[pygame.K_l]:
            filename = "save.pkl"
            print("Load")
            with open(filename, 'rb') as file:
                print("load2")
                world = pickle.load(file)
                GUI1 = GUI(world.getW(), world.getH())
                GUI1.update(world)


pygame.quit()
