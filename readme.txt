Vacuum Cleaner Agents Project

The base class Cleaner (cleaner.py) has the percept and action functionalities.
The Choose() method is for asking the Cleaner to choose an action. In the base
class, its default behavior is to turn off.

We have derived 3 classes from the cleaner class - agentReflex, agentRandom, and agentModel.  Each one overrides the Choose() function and may or may not have some internal data.  In the agentRandom case, we have some data there, but they are stored just for ease of testing, could just as easily be a constant.

space.py - describes how we store and manipulate the grid.

sim.py - holds the main script for testing.  There is a global variable VERBOSE declared in this file which can be used to toggle how much debug information you get.

The allowed arguments to the executable are

-a - test all, will run all 4 input files on all 4 agents.  Used without additional arguments

-x - test the simple reflex agent, requires an input file name to follow.

-r - test the random reflex agent, requires an input file name to follow.

-m - test the model based agent, requires an input file name to follow.