#!/usr/bin/python

'''
Space class

properties:
    IsWall      boolean     is the space a wall?
    IsDirty     boolean     does it contain dirt?
    
If the space is a wall, IsDirty is meaningless and is initialized to False
'''

class Space(object):
    
    def __init__(self, isWall, isDirty):
        self.IsWall = isWall
        if not isWall:
            self.IsDirty = isDirty
        else:
            self.IsDirty = False

    def Clean(self):
        if not self.IsWall:
            self.IsDirty = False



        
