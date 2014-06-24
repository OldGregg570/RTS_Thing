from game.Drawable import Drawable
from game.Colors import Colors
from game.globals import CENTER_X, CENTER_Y
from game.Vector2D import Vector2D

import math
import pygame
from collections import deque

class Player (Drawable):
    '''
    player entity
    '''
    def __init__ (self, position):
        super (Player, self).__init__ (position)
        self.isSelected = False
        self.destinationQueue = deque([])
        self.velocity = Vector2D (0,0) 
        self.currentDestination = self.position
        
    def draw (self, g): 
        self._drawPath(g)
        self._drawPlayer(g)

    def _drawPlayer (self, g):
        if self.isSelected: color = Colors.GREEN
        else:               color = Colors.RED
        x, y = self.position.x, self.position.y
        for n in range (4):
            xOffset = (x - CENTER_X) / (41 - (8 * n))
            yOffset = (y - CENTER_Y) / (41 - (8 * n))
            p = (int (self.position.x + xOffset), 
                int (self.position.y + yOffset))
            pygame.draw.circle(g, color, p, 4)
            
    def _drawPath (self, g):
        if self.velocity.length() > 0:
            current = self.currentDestination
            
            pygame.draw.line(g, Colors.GREEN, (self.position.x, self.position.y), 
                             (self.currentDestination.x, self.currentDestination.y))
            
            for p in self.destinationQueue:
                pygame.draw.line(g, Colors.GREEN, (current.x, current.y), (p.x, p.y))
                current = p       
    
    def move (self):
        if self.isSelected:
            self.velocity = self.currentDestination - self.position
            self.velocity.normalize ()
            displacement = self.position.displacement (self.currentDestination)
            
            if displacement > 10:
                self.position = self.position + self.velocity.scale(4 / displacement)    
            else:
                if self.destinationQueue:
                    self.currentDestination = self.destinationQueue.popleft()
                else:
                    self.currentDestination = self.position
                    self.velocity = Vector2D (0, 0)
                
    def checkCollision (self, other):
        if self.position.displacement (other.position) < 20:
            v = other.position - self.position
            d = v.getDirection ()
            self.nudge(d + math.pi)
            other.nudge (d) 
    
    def addDestination (self, dest):
        if self.currentDestination == self.position:
            self.currentDestination = dest
        else:
            self.destinationQueue.append(dest)
        
        pass
    
    def update (self):
        '''
        update this entity
        '''
        if self.currentDestination:
            self.move()
            
    def nudge (self, direction):
        x = 1.0 * math.sin(direction)
        y = -1.0 * math.cos(direction)
        self.position = self.position + Vector2D (x, y)



 