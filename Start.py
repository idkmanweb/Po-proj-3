from tkinter import *


class Start:
    def __init__(self):
        self.ready = 0
        self.root = Tk()
        self.l1 = Label(self.root, text="Szerokosc:")
        self.l1.pack()
        self.e1 = Entry(self.root, width=10)
        self.e1.pack()
        self.l2 = Label(self.root, text="Wysokosc:")
        self.l2.pack()
        self.e2 = Entry(self.root, width=10)
        self.e2.pack()
        self.b = Button(self.root, text="Ok", command=self.click)
        self.b.pack()
        self.w = 0
        self.h = 0
        self.root.mainloop()

    def click(self):
        self.w = int(self.e1.get())
        self.h = int(self.e2.get())
        self.ready = 1
        self.root.destroy()

    def isReady(self):
        return self.ready

    def returnWH(self):
        return self.w, self.h
