import pygame
import os
from pygame import Surface
from Logger import Logger

s_icon = pygame.image.load(os.path.join("assets", "sheep.png"))
h_icon = pygame.image.load(os.path.join("assets", "human.png"))
b_icon = pygame.image.load(os.path.join("assets", "borscht.png"))
c_icon = pygame.image.load(os.path.join("assets", "cybersheep.png"))
a_icon = pygame.image.load(os.path.join("assets", "antelope.png"))
d_icon = pygame.image.load(os.path.join("assets", "dandelion.png"))
f_icon = pygame.image.load(os.path.join("assets", "fox.png"))
gr_icon = pygame.image.load(os.path.join("assets", "grass.png"))
g_icon = pygame.image.load(os.path.join("assets", "guarana.png"))
n_icon = pygame.image.load(os.path.join("assets", "nightshade.png"))
t_icon = pygame.image.load(os.path.join("assets", "turtle.png"))
w_icon = pygame.image.load(os.path.join("assets", "wolf.png"))


class GUI:

    def __init__(self, w, h):
        self.log = Logger()
        self.tilew = int(600 / w)
        self.tileh = int(600 / h)
        pygame.init()
        self.w = w
        self.h = h
        self.window = pygame.display.set_mode((600, 800))
        self.run = 1
        pygame.display.set_caption("PO proj 3, Piotr Chojnowski 193382")
        pygame.display.set_icon(f_icon)
        self.window.fill((5, 130, 32))
        self.font = pygame.font.SysFont('Arial', 12)
        self.logText = self.font.render(self.log.write(), True, (0, 0, 0), (255, 255, 255))
        self.logArea = Surface((600, 200))
        self.logArea.fill((255, 255, 255))
        self.window.blit(self.logArea, (0, 600))
        self.window.blit(self.logText, (0, 600))
        pygame.display.update()

    def getRun(self):
        return self.run

    def setRun(self, run):
        self.run = run

    def update(self, world):
        for i in range(world.getW()):
            for j in range(world.getH()):
                if world.getMap()[i][j] == 's':
                    self.window.blit(pygame.transform.scale(s_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'h':
                    self.window.blit(pygame.transform.scale(h_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'b':
                    self.window.blit(pygame.transform.scale(b_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'c':
                    self.window.blit(pygame.transform.scale(c_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'a':
                    self.window.blit(pygame.transform.scale(a_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'd':
                    self.window.blit(pygame.transform.scale(d_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'f':
                    self.window.blit(pygame.transform.scale(f_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == '/':
                    self.window.blit(pygame.transform.scale(gr_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'g':
                    self.window.blit(pygame.transform.scale(g_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'n':
                    self.window.blit(pygame.transform.scale(n_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 't':
                    self.window.blit(pygame.transform.scale(t_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
                elif world.getMap()[i][j] == 'w':
                    self.window.blit(pygame.transform.scale(w_icon, (self.tilew, self.tileh)), (i * self.tilew, j * self.tileh))
        self.displayText()
        pygame.display.update()

    def clear(self):
        self.window.fill((5, 130, 32))
        self.window.blit(self.logArea, (0, 600))

    def displayText(self):
        x, y = 0, 600
        lines = [word.split('\n') for word in self.log.write().splitlines()]
        space = self.font.size(' ')[0]
        wordw, wordh = 0, 0
        for line in lines:
            for words in line:
                self.logText = self.font.render(words, True, (0, 0, 0))
                wordw, wordh = self.logText.get_size()
                if x + wordw >= 600:
                    x = 0
                    y += wordh
                self.window.blit(self.logText, (x, y))
                x += wordw + space
            x = 0
            y += wordh

    def getLog(self):
        return self.log
