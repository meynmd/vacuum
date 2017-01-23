#!/usr/bin/python

import sys
import space
import cleaner
import agentReflex
import agentRandom
import agentModel
import agentModelFour

VERBOSE = False

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
	print '\nusage:\ntester {-x | -r | -m | -a} <env filename>\n'


def TestReflexAgent(filename):
	print '************* TESTING REFLEX AGENT ****** ON FILE ' + filename
	agent = agentReflex.ReflexCleaner()
	grid = LoadGrid(filename)

	initDirtCount = CountDirt(grid)
	numAct = agent.Run(grid, VERBOSE)
	cleanedDirtCount = initDirtCount - CountDirt(grid)
	print 'Reflex Agent cleaned ' + str(cleanedDirtCount) + ' of ' + str(initDirtCount) + ' spaces using ' + str(numAct) + ' actions'
	print 'Efficiency: ' + str(float(cleanedDirtCount)/float(numAct)) + '\n%cleaned: '+ str(float(cleanedDirtCount)/float(initDirtCount))

def TestModelAgent(filename):
	print '************* TESTING MODEL AGENT  3 Bit Version ****** ON FILE ' + filename
	agent = agentModel.ModelCleaner()
	grid = LoadGrid(filename)

	initDirtCount = CountDirt(grid)
	numAct = agent.Run(grid, VERBOSE)
	cleanedDirtCount = initDirtCount - CountDirt(grid)
	print 'Model Agent cleaned ' + str(cleanedDirtCount) + ' spaces using ' + str(numAct) + ' actions'
	print 'Efficiency: ' + str(float(cleanedDirtCount) / float(numAct)) + ' \n%cleaned: ' + str(float(cleanedDirtCount) / float(initDirtCount))

	print '************* TESTING MODEL AGENT  4 Bit Version ****** ON FILE ' + filename
	agent = agentModelFour.ModelFourCleaner()
	grid = LoadGrid(filename)

	initDirtCount = CountDirt(grid)
	numAct = agent.Run(grid, VERBOSE)
	cleanedDirtCount = initDirtCount - CountDirt(grid)
	print 'Model Agent cleaned ' + str(cleanedDirtCount) + ' spaces using ' + str(numAct) + ' actions'
	print 'Efficiency: ' + str(float(cleanedDirtCount) / float(numAct)) + ' \n%cleaned: ' + str(float(cleanedDirtCount) / float(initDirtCount))



def TestRandomAgent(filename):
	print '************* TESTING RANDOM AGENT ****** ON FILE ' + filename
	print 'probability to turn off 20%, turn left 33%, turn right 33%, move 33%'
	agent = agentRandom.RandomCleaner(20,33,33)
	sumActions = 0; sumDirts = 0
	#print '\tCleaned Spaces \t Actions Taken'
	for i in range (0,50):
		grid = LoadGrid(filename)
		initDirtCount = CountDirt(grid)
		numAct = agent.Run(grid, VERBOSE)

		cleanedDirtCount = initDirtCount - CountDirt(grid)

		#print str(initDirtCount - endDirtCount) + '\t' + str(numAct)
		sumActions += numAct
		sumDirts += cleanedDirtCount
	print 'Averages \t ' + str(sumDirts/50) + ' ' + str(sumActions/50)
	print 'Efficiency: ' + str(float(sumDirts) / float(sumActions)) + ' \n%cleaned: ' + str(float(sumDirts) / float(initDirtCount*50))

	print '************* TESTING RANDOM AGENT ****** ON FILE ' + filename
	print 'probability to turn off 20%, turn left 15%, turn right 15%, move 70%'
	agent = agentRandom.RandomCleaner(20,15,15)
	sumActions = 0; sumDirts = 0
	#print '\tCleaned Spaces \t Actions Taken'
	for i in range (0,50):
		grid = LoadGrid(filename)
		initDirtCount = CountDirt(grid)
		numAct = agent.Run(grid, VERBOSE)

		cleanedDirtCount = initDirtCount - CountDirt(grid)

		#print str(initDirtCount - endDirtCount) + '\t' + str(numAct)
		sumActions += numAct
		sumDirts += cleanedDirtCount
	print 'Averages \t ' + str(sumDirts/50) + ' ' + str(sumActions/50)
	print 'Efficiency: ' + str(float(sumDirts) / float(sumActions)) + ' \n%cleaned: ' + str(float(sumDirts) / float(initDirtCount*50))


'''
main script

runs one simulation of reflex-agent cleaner
uses environment encoded in first argument to script

'''
if len(sys.argv) < 2:
	PrintUsage()
	quit()

if sys.argv[1] == '-a':
	filenames = ['env1.txt', 'env2.txt', 'env3.txt', 'env4.txt']
	for filename in filenames:
		TestRandomAgent(filename)
		TestReflexAgent(filename)
		TestModelAgent(filename)
		print '\n'
	quit()

if len(sys.argv) !=3:
	PrintUsage()
	quit()

elif sys.argv[1] == '-x':
	TestReflexAgent(sys.argv[2])
elif sys.argv[1] == '-r':
	TestRandomAgent(sys.argv[2])
elif sys.argv[1] == '-m':
	TestModelAgent(sys.argv[2])
else:
	PrintUsage()
	quit()
