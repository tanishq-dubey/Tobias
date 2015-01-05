
from TobiasPyFiles import items, enemies

__author__ = 'Tanishq Dubey'

class Player:

    itemInventory = []
    weaponInventory = []

    hp = 100

    chosenWeapon = None

    ap = 0

    def isPlayerAlive(self):
        return self.hp > 0

    def isPlayerUsingArmor(self):
        return self.ap > 0

    def printItemInventory(self):
        for item in self.itemInventory:
            print(item, '\n')

    def printWeaponInventory(self):
        for items in self.weaponInventory:
            print(items.Weapons, '\n')

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

    def PlayerSetWeapon(self,weaponNumber):
        self.chosenWeapon = weaponNumber

    def CheckPlayerWeapon(self):
        if(self.chosenWeapon is None):
            print("You don't have a weapon equipped! Now would be a decent time to choose one!")
            return False
        else:
            return True

    def PlayerAttack(self,enemy):
        if self.CheckPlayerWeapon():
            damage = self.weaponInventory[self.chosenWeapon].damage
            if enemy.useArmor():
                enemy.ap -= damage
                if enemy.ap <= 0:
                    print("You use your {} against {}, and destroy their armor!")
                else:
                    print("You use your {} against {}, dealing {} damage to their armor!".format(self.weaponInventory[self.chosenWeapon], enemy.name, damage))
            else:
                enemy.hp -= damage
                if enemy.isAlive():
                    print("You use your {} against {}, dealing {} damage to them!".format(self.weaponInventory[self.chosenWeapon], enemy.name, damage))
                else:
                    print("You use your {} against {}, dealing enough damage to kill them!".format(self.weaponInventory[self.chosenWeapon], enemy.name))

        else:
            self.CheckPlayerWeapon()
            return
