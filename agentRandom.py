#!/usr/bin/python

import cleaner
import random

class RandomCleaner(cleaner.Cleaner):

	def __init__(self):
		cleaner.Cleaner.__init__(self)
		random.seed()

	'''
	choose a randomized action based on current percept
	
	grid		2d list of Space	the starting environment
	
	'''
	def Choose(self, grid):
		isFacingWall = self.SenseWall(grid)
		isSpaceDirty = self.SenseDirt(grid)
		isHome = self.SenseHome()

		# if the current space is dirty, should always clean it
		if isSpaceDirty:
			return self.ActSuckDirt

		# if the space is not dirty...
		else:
		
			if isHome:
				if random.randint(0, 5) == 0:
					return self.ActTurnOff

			if isFacingWall:
				return self.TurnRandom()

			else:
				if random.randint(0, 3) == 0:
					return self.TurnRandom()
				else:
					return self.ActMove



	def TurnRandom(self):
		if random.randint(0, 2) == 0:
			return self.ActTurnRight
		else:
			return self.ActTurnLeft






