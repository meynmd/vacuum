#!/usr/bin/python

import sys
import space
import cleaner
import agentReflex
import agentRandom

''' 
load environment from file

filename		string		file containing environment encoding

'''
def LoadGrid(filename):
	grid = []
	gridFile = open(filename)
	for line in gridFile:
		line = line.strip('\n')
		words = line.split('\t')
		
		row = []
		for word in words:
		
			# find out if the space is a wall, is clean or dirty
			isDirty = False
			isWall = False
			if word == 'w':
				isWall = True
			else:
				isWall = False

				if word == 'c':
					isDirty = False
				elif word == 'd':
					isDirty = True
				else:
					print 'Error reading file: use w, c or d for spaces'

			row.append(space.Space(isWall, isDirty))

		grid.insert(0, row)

	return grid



'''
interactive (console) test of cleaner base class

gridFile		string		file encoding environment to test

1 moves forward
2 sucks up dirt
9 turns left
0 turns right

'''
def consTest(gridFile):
	grid = LoadGrid(gridFile)
	c = cleaner.Cleaner()

	while True:
		c.PrintInfo()
		print 'Is at Home location?'
		print str(c.SenseHome())
		print 'Is there a wall in front?'
		print str(c.SenseWall(grid))
		print 'Is this square dirty?'
		print str(c.SenseDirt(grid))

		inp = input(': ')
		if inp == 1:
			c.Move(grid)
		elif inp == 2:
			c.SuckDirt(grid)
		elif inp == 9:
			c.Turn(0)
		elif inp == 0:
			c.Turn(1)

		print



'''
count how many spaces in grid are dirty

grid		2d list of spaces

'''
def CountDirt(grid):
	count = 0
	for row in grid:
		for space in row:
			if space.IsDirty:
				count += 1
	return count



def PrintUsage():
	print '\nusage:\ntester {-x | -r | -m} <env filename>\n'



'''
main script

runs one simulation of reflex-agent cleaner
uses environment encoded in first argument to script

'''
if len(sys.argv) != 3:
	PrintUsage()
	quit()

grid = LoadGrid(sys.argv[2])

initDirtCount = CountDirt(grid)

if sys.argv[1] == '-x':
	agent = agentReflex.ReflexCleaner()
elif sys.argv[1] == '-r':
	agent = agentRandom.RandomCleaner()
else:
	PrintUsage()
	quit()


numAct = agent.Run(grid)

endDirtCount = CountDirt(grid)

print '\nCleaned ' + str(initDirtCount - endDirtCount) + ' spaces.'
print 'Took ' + str(numAct) + ' actions.\n'
