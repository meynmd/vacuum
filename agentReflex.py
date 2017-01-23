#!/usr/bin/python

import cleaner

class ReflexCleaner(cleaner.Cleaner):

	'''
	choose an action based on current percept
	
	grid		2d list of Space	the starting environment
	
	'''
	def Choose(self, grid):
		#print 'beginning to choose action'
		isFacingWall = self.SenseWall(grid)
		isSpaceDirty = self.SenseDirt(grid)
		isHome = self.SenseHome()

		# if the current space is dirty, clean it
		if isSpaceDirty:
			return self.ActSuckDirt

		# if the space is not dirty...
		else:
		
			if not isFacingWall:
				return self.ActMove
			
			# if there's a wall in front,
			# turn off or go a different direction
			else:
			
				if isHome:
					return self.ActTurnOff
				else:
					return self.ActTurnRight




