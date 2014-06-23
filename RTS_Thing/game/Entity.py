
from game.Drawable import Drawable
from game.Vector2D import Vector2D
import math

class Entity (Drawable):
    '''
    drawable class with a destination
    '''
    def __init__ (self, position):
        super (Entity, self).__init__ (position)
        self.destination = self.position
        self.velocity = Vector2D (0,0)

    def setDestination (self, p):
        self.destination = p

    def update (self):
        '''
        update this entity
        '''
        if self.destination:
            self.move()
    def move (self):
        self.velocity = self.destination - self.position
        self.velocity.normalize ()
        displacement = self.position.displacement (self.destination)
        
        if displacement > 10:
            self.position = self.position + self.velocity.scale(5 / displacement)    
        else:
            self.destination = self.position
            self.velocity = Vector2D (0, 0)
            
    def nudge (self, direction):
        x = 1.0 * math.sin(direction)
        y = -1.0 * math.cos(direction)
        self.position = self.position + Vector2D (x, y)



 
            
            

