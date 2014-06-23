from game.Vector2D import Vector2D
from game.Colors import Colors
import pygame


class Drawable (object):
    '''
    a drawable object
    '''
    def __init__ (self, position):
        self.position = position
        super (Drawable, self).__init__ ()

    def draw (self, g):
        '''
        draw this object
        '''
        p1 = self.position - Vector2D (2, 2)
        p2 = self.position + Vector2D (2, 2)
        
        
        pygame.draw.line(g, Colors.RED, (p1.x, p1.y) , (p2.x, p2.y) )
        
    



 

    

        

