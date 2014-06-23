
from game.Drawable import Drawable
from game.Vector2D import Vector2D
from game.globals import ORIGIN, SCREEN_SIZE
import pygame

class Background (Drawable):
    '''
    drawable background object
    '''
    def __init__ (self):
        super (Background, self).__init__ (Vector2D (0,0))
    
    def draw (self, g):
        '''
        fill the screen with a solid blackish rectangle
        '''
        super (Background, self).draw (g)
        pygame.draw.rect (g, (20, 25, 25), (ORIGIN, SCREEN_SIZE))
    
    