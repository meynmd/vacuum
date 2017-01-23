#!/usr/bin/python

import space



'''
print representation of grid to screen

grid		2d list of Space
cleaner		reference to Cleaner object (so we can see where it is)

'''
def PrintGrid(grid, cleaner):
	x, y = cleaner.Location
	rot = cleaner.Rotation
	rowCount = 0
	for i in range(len(grid) - 1, -1, -1):
		line = ''
		for j in range(len(grid[0])):
			space = grid[i][j]
			if i == y and j == x:
				if rot == 0:
					line = line + '^'
				elif rot == 1:
					line = line + '>'
				elif rot == 2:
					line = line + 'v'
				else:
					line = line + '<'

			elif space.IsWall:
				line = line + 'X'
			elif space.IsDirty:
				line = line + 'D'
			else:
				line = line + ' '

			line = line + ' '
		print line
	print




'''
Cleaner class

vacuum cleaning base class

'''
class Cleaner(object):

	Up = 0
	Right = 1
	Down = 2
	Left = 3
	NumDirections = 1 + Left
	Home = (1, 1)
	
	# commands
	ActMove = 0
	ActTurnRight = 1
	ActTurnLeft = 2
	ActSuckDirt = 3
	ActTurnOff = 4

	''' 
	initialize the object
	
	'''
	def __init__(self):
		self.Location = self.Home
		self.Rotation = self.Up


	'''
	turn the cleaner
	
	direction		int			1 for clockwise, 0 for counterclockwise
	
	'''
	def Turn(self, direction):
		if direction == 1:
			self.Rotation = (self.Rotation + 1) % self.NumDirections
		else:
			self.Rotation = (self.Rotation - 1 + self.NumDirections) \
							% self.NumDirections


		
		
	'''
	utility function to find coords of space in front of vacuum cleaner
	
	'''
	def GetSpaceInFront(self):
		x, y = self.Location
		if self.Rotation == self.Up:
			y += 1
		elif self.Rotation == self.Right:
			x += 1
		elif self.Rotation == self.Down:
			y -= 1
		else:
			x -= 1
		return (x, y)



	'''
	sense if the space in front is a wall
	
	grid		2d list of spaces
	
	'''
	def SenseWall(self, grid):
		x, y = self.GetSpaceInFront()

		if x <= 0 or x >= len(grid[y]) - 1:
			return True
		if y <= 0 or y >= len(grid) - 1:
			return True

		return grid[y][x].IsWall

		
	'''
	sense if the current space is dirty
	
	grid		2d list of spaces

	'''
	def SenseDirt(self, grid):
		x, y = self.Location
		return grid[y][x].IsDirty
	


	'''
	sense if the vacuum cleaner is at the home location
	
	'''
	def SenseHome(self):
		return self.Location == self.Home


	'''
	move the cleaner forward, if possible return true, otherwise return false
	
	'''
	def Move(self, grid):
		if self.SenseWall(grid):
			return False
		
		x, y = self.GetSpaceInFront()
		if x <= 0 or x >= len(grid[y]) - 1:
			return False
		if y <= 0 or y >= len(grid) - 1:
			return False

		self.Location = (x, y)
		return True


	'''
	suck up dirt on the current space
	
	'''
	def SuckDirt(self, grid):
		x, y = self.Location
		grid[y][x].Clean()



	def Choose(self, grid):
		return self.ActTurnOff


	'''
	run the simulation
	
	'''
	def Run(self, grid):
		numActions = 0
	
		# run until the machine decides to shut down
		while True:
			#self.PrintInfo()
			#print 'ya I am here'
			PrintGrid(grid, self)
			#s = raw_input()
			action = self.Choose(grid)
			
			numActions += 1
			
			if action == self.ActMove:
				#print 'Moving forward'
				self.Move(grid)
			elif action == self.ActTurnRight:
				#print 'Turning right'

				self.Turn(1)
				#if self.SenseWall(grid):
				#	self.Turn(1)
			elif action == self.ActTurnLeft:
				#print 'Turning left'

				self.Turn(0)
				#if self.SenseWall(grid):
				#	self.Turn(0)
			elif action == self.ActSuckDirt:
				#print 'Sucking dirt'
				self.SuckDirt(grid)
			elif action == self.ActTurnOff:
				print '\nTurning off.\n'
				return numActions

			print


	'''
	print the position and rotation of the vacuum cleaner
	
	'''
	def PrintInfo(self):
		if self.Rotation == self.Up:
			rot = 'Up'
		elif self.Rotation == self.Right:
			rot = 'Right'
		elif self.Rotation == self.Down:
			rot = 'Down'
		else:
			rot = 'Left'

		print 'Location: ' + str(self.Location)
		print 'Rotation: ' + rot

