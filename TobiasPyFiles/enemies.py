class Enemy(object):
    def __init__(self, name, description, hp, ap, damage):
        self.name = name
        self.description = description
        self.hp = hp
        self.ap = ap
        self.damage = damage

    def __str__(self):
        return "{}:\n{}\nHealth: {}\t Armor: {}\n".format(self.name, self.description, self.hp,self.ap)

    def is_alive(self):
        return self.hp > 0

    def uses_armor(self):
        return self.ap > 0


class SpacePirate(Enemy):
    def __init__(self):
        super(SpacePirate, self).__init__(name="Space Pirate", description="A scurvy bandit who just wants your money, and you're in his way", hp= 10, ap=0, damage=2)

class RobotUnderling(Enemy):
    def __init__(self):
        super(RobotUnderling, self).__init__(name="Robot Underling", description="A simple minded robot that tries its best to aim for you (it really does).", hp=20, ap=0, damage=5)


class RobotOverlord(Enemy):
    def __init__(self):
        super(RobotOverlord, self).__init__(name="Robot Overlord", description="So this is what those mad scientists were talking about when they said robot annihilation.", hp=75, ap=25, damage=20)
