from TobiasPyFiles import items, enemies

__author__ = 'Martin'

class MapSpace(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def intro_text(self):
        raise NotImplementedError()
    def modify_player(self, player):
        raise NotImplementedError()

class InitialRoom(MapSpace):
    def intro_text(self):
        return """
        Tobias stood there, choosing between doors that might lead to his impending doom
        """

    def modify_player(self, player):
        #Room has no action on player
        pass

class ItemRoom(MapSpace):
    def __init__(self, x, y, item):
        self.item = item
        super(ItemRoom, self).__init__(x, y)

    def add_loot(self, player):
        player.inventory.append(self.item)

    def modify_player(self, player):
        self.add_loot(player)

class HostileRoom(MapSpace):
    def __init__(self, x, y, enemy):
        self.enemy = enemy
        super(HostileRoom, self).__init__(x, y)

    def modify_player(self, the_player):
        if self.enemy.is_alive():
            the_player.hp = the_player.hp - self.enemy.damage
            print("Entity does {} damage. You're down to {} HP.".format(self.enemy.damage, the_player.hp))
