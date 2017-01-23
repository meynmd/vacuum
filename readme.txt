Vacuum Cleaner Agents Project

The base class Cleaner (cleaner.py) has the percept and action functionalities.
The Choose() method is for asking the Cleaner to choose an action. In the base
class, its default behavior is to turn off.

[TODO]
I guess the base class should also have fields for state so that the Model Agent
can use them.

Specific agent programs should be implemented in ReflexCleaner class
(agentReflex.py), RandomCleaner class (agentRandom.py) and [TODO] ModelCleaner
class (agentModel.py).

space.py contains a simple class to represent a space on the grid, which is a
wall or is not; and is dirty or is not.

The grid is represented as a 2d array (list of lists) of Space objects.

The main script is sim (a Python script, but who wants to keep typing .py?).
Its first argument is -x, -r, or -m (refleX, Random, or Model-based). Second
argument is environment file (env1.txt or env2.txt).
