"""Class for all items found within the game.

-Item is the main class that contains the basic data for all items in the game.
    -Name of the item.
    -Description of the item.
    -Value of the item (in the case of gold or currency, same as the amount/quantity).
    -str: return a simple format line about the item
-Specific items, such as quest items, will inherit the "Item" class and add their own attributes as needed.
"""

__author__ = 'Tanishq Dubey'


class Item():
    def __init__(self, name, description, value):
        self.name = name
        self.description = description
        self.value = value

    def __str__(self):
        return "{}\n:\n{}\nValue: {}\n".format(self.name, self.description, self.value)


class Gold(Item):
    def __init__(self, amount):
        self.amount = amount
        super(Gold, self).__init__(name="Gold", description="The standard unit of trade around here", value=amount)


class Weapons(Item):
    def __init__(self, name, description, value, damage):
        self.damage = damage
        super(Weapons, self).__init__(name, description, value)

    def __str__(self):
        return "{}\n:\n{}\nValue: {}\nDamage: {}\n".format(self.name, self.description, self.value, self.damage)