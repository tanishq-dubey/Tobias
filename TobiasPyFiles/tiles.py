from TobiasPyFiles import items, enemies, actions, world

__author__ = 'Tanishq Dubey'

class Maptile:
	def __init__(self, x, y):
		self.x =x
		self.y =y

	def intro_text(self):
		raise NotImplementedError()

	def modify_player(self, player):
		raise NotImplementedError()

	def adjacent_moves(self):
		moves = []
		if world.tile.exists(self.x + 1, self.y):
			moves.append(actions.MoveEast())
		if world.tile.exists(self.x - 1, self.y):
			moves.append(actions.MoveWest())
		if world.tile.exists(self.x, self.y + 1):
			moves.append(actions.MoveNorth())
		if world.tile.exists(self.x + 1, self.y -1):
			moves.append(actions.MoveSouth())

	def available_actions(self):
		moves = self.adjacent_moves()
		moves.append(actions.ViewInventory())
		return moves

class StartingRoom(Maptile):
	def intro_text(self):
		return """
		You awaken in the hold of a star ship.
		Your programming tells you that it is a Federation Cruiser.
		How did you end up here?
		"""

	def modify_player(self, player):
		pass

class EndingRoom(Maptile):
	def intro_text(self):
		return"""
		You enter a room with a large cylindrical chamber in the center.
		Your sensors tell you that there are multiple nuclear vibrations coming from
		the cylinder...
		... in fact, they match the adaptive subpsace echograms for interdimentional 
		warps!

		Before you know it, there is a flash of light and you are sucked into the machine
		flying through space!
		"""

	def modify_player(self, player):
		player.victory = True

class LootRoom(Maptile):
	def __init__(self, x, y, item):
		self.item = item
		super().__init__(x, y)

	def add_loot(self, player):
		player.inventory.append(self.item)

	def modify_player(self, player):
		self.add_loot(player)

class EnemyRoom(Maptile):
	def __init__(self, x, y, enemy):
		self.enemy = enemy
		super().__init__(x, y)

	def modify_player(self, the_player):
		if self.enemy.is_alive():
			the_player.hp = the_player.hp - self.enemy.damage
			print("{} does {} damage to you! You have {} HP remaining.".format(self.enemy.name, self.enemy.damage, the_player.hp))

	def available_actions(self):
		if self.enemy.is_alive():
			return	(actions.Flee(tile=self), actions.Attack(enemy=self.enemy))
		else:
			return self.adjacent_moves()

class EmptyShipHallway(Maptile):
	def intro_text(self):
		return"""
		You find yourself in another brightly lit hallway. Not much different from the
		rest of the ship. There is nothing here to explore.
		"""

	def modify_player(self, player):
		pass

class RobotUnderlingRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.RobotUnderling)

	def intro_text(self):
		if self.enemy.is_alive():
			return"""
			As you enter the room, a curious looking robot turns to face you
			'KILL ALL INTRUDERS' it screams!
			"""
		else:
			return"""
			The burnt metal remains of the Robot Underling remain scattered on the ground
			"""

class SpacePirateRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.SpacePirate())

	def intro_text(self):
		if self.enemy.is_alive():
			return"""
			'You chose the wrong day to be on this ship little guy' says a tall human pirate.
			Before you know it, he has pulled out his weapon!
			"""
		else:
			return"""
			The corpse of a space pirate lays on the ground.
			"""

class RobotOverlordRoom(EnemyRoom):
	def __init__(self, x, y):
		super().__init__(x, y, enemies.RobotOverlord())

	def intro_text(self):
		if self.enemy.is_alive():
			return"""
			You enter the room and are surprised to find a large shadow blocking all the lights.
			As you look up, you see a behemoth robot towering above you, charging its weapons.
			"""
		else:
			return"""
			The walls remain charred from your battle with the Robot Overlord.
			"""

class FindMetoriteSaberRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.MetoriteSaber())

	def intro_text(self):
		return"""
		A glimmer on the floor catches your attention.
		You investigate and find a Metorite Saber!
		This weapon is favored by pirates for its light weight and strength.
		"""

class FindBlasterPistol(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.BlasterPistol())

	def intro_text(self):
		return"""
		As you enter the room, something hits your foot.
		A standard issue Federation Blaster Pistol!
		"""

class FindBossWeapon(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.BossWeapon())

	def intro_text(self):
		return"""
		A blue pulsating light fills the chamber. Mounted on the wall, you see the holy-grail of all weapons.
		The AX-36 MatchMaker. 
		"""

class FindGoldRoom(LootRoom):
	def __init__(self, x, y):
		super().__init__(x, y, items.BossWeapon())

	def intro_text(self):
		return"""
		You see a few Galatic Credits scattered about the floor and quickly pick them up.
		"""