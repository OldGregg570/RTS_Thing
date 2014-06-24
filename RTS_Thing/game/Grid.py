
from game.Drawable import Drawable
from game.Vector2D import Vector2D
from game.Colors import Colors
import pygame
import math
import queue


GRID_SPACING = 10

R = Colors.getShade(.2, Colors.RED)
G = Colors.getShade(.2, Colors.GREEN)
B = Colors.getShade(.2, Colors.BLUE)


class Node (Drawable):
    
    def __init__ (self, x, y, n, e, s, w, c = G):
        super (Node, self).__init__ (Vector2D (0,0))
        self.x = x
        self.y = y
        self.neighbors = (n, e, s, w)
        self.previousNode = None
        self.color = c
        
    def draw (self, g):
        pygame.draw.circle (g, self.color, (self.x * GRID_SPACING + 1, self.y * GRID_SPACING + 1), 2)
    
    def reset (self):
        self.previousNode = None
        

class Grid (Drawable):
    '''
    size: tuple (800, 600) or something like that
    
    Grid class used for player pathfinding
    '''
    NIL = Node (-1, -1, None, None, None, None)
    def __init__ (self, size, walls = []):
        super (Grid, self).__init__ (Vector2D (0,0))
        self.nodes = []
        self.size = size
        w = self.width = int (self.size [0] / GRID_SPACING) + 1
        h = self.height = int (self.size [1] / GRID_SPACING) + 1
        for y in range (self.height):
            for x in range (self.width):
                n, e, s, w = (0, -1), (1, 0), (0, 1), (-1, 0)
                if x == 0:      n = None
                if y == 0:      w = None
                if x == w:      e = None
                if y == h:      s = None
                
                if x == 40 and (y < 40 or y > 45):
                    self.nodes.append (Grid.NIL)
                else:
                    self.nodes.append (Node (x, y, n, e, s, w))
        pass
        
    def reset (self):
        '''
        Initialize the grid
        '''
        for n in self.nodes:
            n.reset ()

            
    def draw (self, g):
        for n in self.nodes:
            n.draw (g)             
    
    def getClosestNodePosition (self, position):
        x = math.floor (position.x / GRID_SPACING) * GRID_SPACING
        y = math.floor (position.y / GRID_SPACING) * GRID_SPACING
        return Vector2D (x, y)
    
    def getNodeAt (self, position):
        p = self.getClosestNodePosition (position)
        i = self.getNodeIndex (p.x / GRID_SPACING, p.y / GRID_SPACING)
        return self.nodes [i]
            
    def shortestPath (self, source, dest):
        self.reset()
        nodeQueue = queue.Queue ()
        nodeQueue.put_nowait (source)
        source.previousNode = Grid.NIL
        
        while not nodeQueue.empty ():
            currentNode = nodeQueue.get_nowait ()
            
            if currentNode == dest:
                while not nodeQueue.empty ():
                    nodeQueue.get_nowait ()
                return currentNode
            else:
                currentNode.color = R
                for n in currentNode.neighbors:
                    if n:
                        index = self.getNodeIndex (currentNode.x + n[0], currentNode.y + n[1])
                        if index:
                            neighbor = self.nodes [index]
                            if (neighbor and
                                neighbor.previousNode == None):
                                neighbor.previousNode = currentNode
                                nodeQueue.put (neighbor)
        return
            
    def getNodeIndex (self, x, y):
        i = (y * self.width) + x
        if x >= 0 and y >= 0 and x < self.width and y < self.height:
            return int (i)
        else:
            return None
        
        