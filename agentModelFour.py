#!/usr/bin/python

import cleaner


class Enum(set):
    def __getattr__(self, name):
        if name in self:
            return name
        raise AttributeError

Directions = Enum(["RIGHT", "LEFT"])

class ModelFourCleaner(cleaner.Cleaner):

	def __init__(self):
		cleaner.Cleaner.__init__(self)
		
		# 4 bits of memory
		self.isSweepingNorth = True
		self.isStartingTurn = False
		self.isDoneTurning = True
		self.isReversed = False


	def ReversedTurn(self, dir):
		if dir == Directions.RIGHT:
			if self.isReversed:
				return self.ActTurnLeft
			else:
				return self.ActTurnRight
		else: #if Directions.LEFT:
			if self.isReversed:
				return self.ActTurnRight
			else:
				return self.ActTurnLeft

	'''
	choose an action based on current percept

	grid		2d list of Space	the starting environment
	NextAction ==1 -> Turn
	isFacingWall==1
	'''
	def Choose(self, grid):
		hitWall = self.SenseWall(grid)
		sweepingNorth = self.isSweepingNorth
		turnStarted = self.isStartingTurn
		turnDone = self.isDoneTurning

		if self.SenseDirt(grid):
			return self.ActSuckDirt
		if self.SenseHome() and self.isReversed:
			return self.ActTurnOff

		if not hitWall and not turnStarted and turnDone: 					# Rule 1, straight line N or S
			return self.ActMove

		if hitWall and not turnStarted and turnDone and sweepingNorth:		# Rule 2, turning after moving N
			#print 'executing 2'
			self.isStartingTurn = True; self.isDoneTurning = False
			return self.ReversedTurn(Directions.RIGHT)

		if not hitWall and turnStarted and not turnDone:					# Rule 3, move after first turn
			#print 'executing 3'
			self.isStartingTurn = False
			return self.ActMove

		if not hitWall and not turnStarted and not turnDone and sweepingNorth:		# Rule 4, turn after move on N
			#print 'executing 4'
			self.isDoneTurning = True
			self.isSweepingNorth = False
			return self.ReversedTurn(Directions.RIGHT)

		if hitWall and not turnStarted and turnDone and not sweepingNorth:			# Rule 5, turning after moving S
			#print 'executing 5'
			self.isStartingTurn = True; self.isDoneTurning = False
			return self.ReversedTurn(Directions.LEFT)

		if not hitWall and not turnStarted and not turnDone and not sweepingNorth:		# Rule 6, turn after move on S
			#print 'executing 6'
			self.isDoneTurning = True
			self.isSweepingNorth = True
			return self.ReversedTurn(Directions.LEFT)

		if hitWall and not turnStarted and not turnDone and sweepingNorth:		# Rule 7, hit wall after first move of U turn at N
			self.isDoneTurning = True
			self.isSweepingNorth = False
			return self.ReversedTurn(Directions.RIGHT) # note that we just flipped the reverse, so this gets strange

		if hitWall and turnStarted and not turnDone and sweepingNorth:		# Rule 8, hit wall after second move of U turn at N
			self.isReversed = True
			self.isDoneTurning = True
			self.isStartingTurn = False
			self.isSweepingNorth = False
			return self.ReversedTurn(Directions.LEFT) # note that we just flipped the reverse, so this gets strange

		if hitWall and not turnStarted and not turnDone and not sweepingNorth:		# Rule 9, hit wall after first move of U turn at S
			self.isDoneTurning = True
			self.isSweepingNorth = True
			return self.ReversedTurn(Directions.LEFT) # note that we just flipped the reverse, so this gets strange

		if hitWall and turnStarted and not turnDone and not sweepingNorth:		# Rule 10, hit wall after second move of U turn at S
			self.isReversed = True
			self.isDoneTurning = True
			self.isStartingTurn = False
			self.isSweepingNorth = True
			return self.ReversedTurn(Directions.RIGHT) # note that we just flipped the reverse, so this gets strange


		else:
			print 'PANIC ********************'
			print hitWall
			print turnStarted
			print turnDone
			print sweepingNorth
			return self.ActTurnOff