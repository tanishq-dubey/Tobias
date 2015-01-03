
from TobiasPyFiles import items

__author__ = 'Tanishq Dubey'

class Player:

    inventory = []

    hp = 100

    def isPlayerAlive(self):
        return self.hp > 0

    def printInventory(self):
        for item in self.inventory:
            print(item, '\n')

    def move(self, dx, dy):
        self.locationX += dx
        self.locationY += dy

    def moveNorth(self):
        self.move(dx=0, dy=-1)

    def moveSouth(self):
        self.move(dx=0, dy=1)

    def moveEast(self):
        self.move(dx=1, dy=0)

    def moveWest(self):
        self.move(dx=-1, dy=0)