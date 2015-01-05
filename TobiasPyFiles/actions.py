from TobiasPyFiles.player import Player

__author__ = 'Tanishq Dubey'

class Action(object):
    def __init__(self, method, name, hotkey, **kwargs):
        self.method = method
        self.hotkey = hotkey
        self.name = name
        self.kwargs = kwargs

    def __str__(self):
        return "{}: {}".format(self.hotkey, self.name)

class MoveNorth(Action):
    def __init__(self):
        super(MoveNorth, self).__init__(method=Player.moveNorth, name='Move north', hotkey='w')


class MoveSouth(Action):
    def __init__(self):
        super(MoveSouth, self).__init__(method=Player.moveSouth, name='Move south', hotkey='s')


class MoveEast(Action):
    def __init__(self):
        super(MoveEast, self).__init__(method=Player.moveEast, name='Move east', hotkey='d')


class MoveWest(Action):
    def __init__(self):
        super(MoveWest, self).__init__(method=Player.moveWest, name='Move west', hotkey='a')

class ViewItemInventory(Action):
    def __init__(self):
        super(ViewItemInventory, self).__init__(method=Player.printItemInventory, name="View Item Inventory", hotkey='i')

class Attack(Action):
    def __init__(self, enemy):
            super(Attack, self).__init__(method=Player.PlayerAttack, name="Attack", hotkey='k',enemy = enemy)