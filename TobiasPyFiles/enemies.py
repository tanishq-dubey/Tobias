"""Class for all enemies found within the game

-Enemy is the main class that contains the basic data for all enemies within the game
    -Name of the enemy (or type of the enemy, if not a specific enemy)
    -Description of the enemy
    -HP (Hit/Health points of the enemy)
    -AP (Armor Points of the enemy, these must be depleted first)
    -Special, such as residual damage or something, can just be a int for different types of specials

"""

__author__ = 'Tanishq Dubey'


class Enemy():
    def __init__(self, name, description, hp, ap, special):
        self.name = name
        self.description = description
        self.hp = hp
        self.ap = ap
        self.special = special

    def isAlive(self):
        return self.hp > 0

    def useArmor(self):
        return self.ap > 0


class RobotUnderling(Enemy):
    def __init__(self):
        super(RobotUnderling, self).__init__(name="Robot Underling", description="A simple minded robot that tries its best to aim for you (it really does).", hp=20, a=0, special=0)


class RobotOverlord(Enemy):
    def __init__(self):
        super(RobotOverlord, self).__init__(name="Robot Overlord", description="So this is what those mad scientists were talking about when they said robot annilation.", hp=75, ap=25, special=2)
