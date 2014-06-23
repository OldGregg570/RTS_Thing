
from game.Drawable import Drawable
from game.Vector2D import Vector2D
from game.Colors import Colors
import pygame
import math
GRID_SPACING = 10

class Node (Drawable):
    def __init__ (self, position, n = True, e = True, s = True, w = True):
        super (Node, self).__init__ (position)
        self.x = position.x
        self.y = position.y
        self.north = n
        self.east = e
        self.south = s
        self.west = w
        
    def draw (self, g):
        pygame.draw.circle (g, Colors.GREEN, (self.x * GRID_SPACING + 1, self.y * GRID_SPACING + 1), 3)
    


class Grid (Drawable):
    def __init__ (self, size):
        super (Grid, self).__init__ (Vector2D (0,0))
        width = int (size [0] / GRID_SPACING) + 1
        height = int (size [1] / GRID_SPACING) + 1
        self.nodes = []
        for x in range (width):
            for y in range (height):
                n, e, s, w = True, True, True, True
                if x == 0:      n = False
                if y == 0:      w = False
                if x == width:  e = False
                if y == height: s = False
                self.nodes.append (Node (Vector2D (x, y), n, e, s, w))
                
    def draw (self, g):
        for n in self.nodes:
            n.draw (g)             
    
    def getClosestNode (self, position):
        x = math.floor (position.x / GRID_SPACING) * GRID_SPACING
        y = math.floor (position.y / GRID_SPACING) * GRID_SPACING
        return Vector2D (x, y)
        
         
        
        
        