#!/usr/bin/python

import cleaner

class ModelCleaner(cleaner.Cleaner):

	def __init__(self):
		cleaner.Cleaner.__init__(self)
		
		# 3 bits of memory
		
		self.IsSweepingNorth = True
		self.NextAction = 0				# 0 == move, 1 == turn
	

	'''
	choose an action based on current percept
	
	grid		2d list of Space	the starting environment
	
	'''
	def Choose(self, grid):
		isFacingWall = self.SenseWall(grid)
		isSpaceDirty = self.SenseDirt(grid)
		isHome = self.SenseHome()

		if isSpaceDirty:
			return self.ActSuckDirt

		else:	# space not dirty
		
			if isFacingWall and self.IsSweepingNorth:
				self.NextAction = 1
				self.IsSweepingNorth = not self.IsSweepingNorth
				return self.ActTurnRight

			elif isFacingWall and not self.IsSweepingNorth:
				self.NextAction = 1
				self.IsSweepingNorth = not self.IsSweepingNorth
				return self.ActTurnLeft

			# not facing wall
			else:
				if self.NextAction == 0:
					self.NextAction = not self.NextAction
					return self.ActMove

				else:
					if not self.IsSweepingNorth:
						self.NextAction = 0
						return self.ActTurnRight
					else:
						self.NextAction = 0
						return self.ActTurnLeft



