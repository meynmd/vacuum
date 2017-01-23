#!/usr/bin/python

import cleaner
import random

class RandomCleaner(cleaner.Cleaner):

	def __init__(self, probTurnOff, probTurnLeft, probTurnRight):
		cleaner.Cleaner.__init__(self)
		random.seed()

		self.probTurnOff = probTurnOff
		self.probTurnLeft = probTurnLeft
		self.probTurnRight = probTurnRight
		self.probMove = 100 - self.probTurnLeft - self.probTurnLeft

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
				if random.randint(0, 100) < self.probTurnOff:
					return self.ActTurnOff

			if isFacingWall:
				randNum = random.randint(0, self.probTurnLeft + self.probTurnRight)
				if randNum < self.probTurnLeft:
					return self.ActTurnLeft
				else:
					return self.ActTurnRight

			else:
				randNum = random.randint(0,100)
				if randNum < self.probTurnLeft:
					return self.ActTurnLeft
				elif randNum < self.probTurnLeft + self.probTurnRight:
					return self.ActTurnRight
				else:
					return self.ActMove



	def TurnRandom(self):
		if random.randint(0, 2) == 0:
			return self.ActTurnRight
		else:
			return self.ActTurnLeft






