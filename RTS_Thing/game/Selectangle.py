from game.Drawable import Drawable
from game.Colors import Colors
import pygame



class Selectangle (Drawable):
    '''
    a drawable object
    '''
    def __init__ (self, position):
        super (Selectangle, self).__init__ (position)
        self.release = position
        
    def draw (self, g):
        '''
        draw this object
        '''
        
        if self.position and self.release:
            if self.release != self.position:
                x = self.position [0]
                y = self.position [1]
                w = self.release[0] - x
                h = self.release[1] - y
                ##s = pygame.Surface ((abs (w), abs (h)))
                r = pygame.Rect (x, y, w, h)
                pygame.draw.rect(g, Colors.GREEN, r, 1)  
                ##s.set_alpha(75)  
                ##g.blit (s, self.position)
            
    def contains (self, p):
        
        # Flip if our selectangle is going backwards
        if self.release [0] < self.position [0]:
            self.release, self.position = ((self.position [0], self.release [1]), 
                                           (self.release [0], self.position [1]))
                        
        if self.release [1] < self.position [1]:  
            self.release, self.position = ((self.release [0], self.position [1]), 
                                           (self.position [0], self.release [1]))
         
        rx = self.position [0]
        ry = self.position [1]
        px = p.x
        py = p.y
        w = self.release[0] - rx
        h = self.release[1] - ry
        rPoint = pygame.Rect (px, py, 0, 0)
        rSelect = pygame.Rect (rx, ry, w, h)
        if rSelect.contains (rPoint):
            return True
        else:
            return False
         
        