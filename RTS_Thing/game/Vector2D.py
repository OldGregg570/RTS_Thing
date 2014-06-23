import math


class Vector2D (object):
    '''
    2D vector class
    '''
    def __init__ (self, x, y):
        self.x, self.y = x, y
    
    def __add__ (self, other):
        '''
        add two vectors
        '''
        return Vector2D (self.x + other.x, self.y + other.y)

    def __sub__ (self, other):
        '''
        subtract two vectors
        '''
        return Vector2D (self.x - other.x, self.y - other.y)
    
    def scale (self, factor):
        return Vector2D (int (self.x * factor), int(self.y * factor))
    
    def normalize (self):
        length = self.length()
        if length != 0:
            return self.scale (1 / length)
        else:
            return self.scale (1)
    
    def length (self):
        return self.displacement(Vector2D (0,0))
    
    def displacement (self, other):
        return math.hypot(self.x - other.x, self.y - other.y)
    
    def getDirection (self):
        if self.x == 0:
            if self.y > 0:
                return math.pi
            else:
                return 0 
        else:
            return math.atan (self.y / self.x)
    
 